import psycopg2
import csv

# Function to connect to PostgreSQL and create the table
def create_table_and_insert_data(csv_file, db_name, user, password, host, port):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cur = conn.cursor()

        cur.execute("""
        DROP TABLE IF EXISTS transit_routes;
        """)
        conn.commit()

        # Create table with a composite primary key
        cur.execute("""
        
        CREATE TABLE IF NOT EXISTS transit_routes (
            agency_id TEXT,
            route_id TEXT,
            route_short_name TEXT,
            route_long_name TEXT,
            PRIMARY KEY (route_id)
        );
        """)
        conn.commit()


        # Read the CSV and insert data
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                agency_id = row['agency_id']
                route_id = row['route_id']
                route_short_name = row['route_short_name']
                route_long_name = row['route_long_name']

                if agency_id != '' and route_id != '' and route_short_name != '' and route_long_name != '':

                    cur.execute("""
                    INSERT INTO transit_routes (agency_id, route_id, route_short_name, route_long_name)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (route_id) DO NOTHING;
                    """, (agency_id, route_id, route_short_name, route_long_name))

        conn.commit()
        cur.close()
        conn.close()
        print("Data inserted successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Function to save database connection details to a file
def save_db_config(file_name, db_name, user, password, host, port):
    with open(file_name, 'w') as file:
        file.write(f"dbname={db_name}\nuser={user}\npassword={password}\nhost={host}\nport={port}")

# Usage
csv_file = 'routes.csv'  # Your CSV file path
db_name = 'transit_db'
user = 'jack'
password = 'xfiles'
host = 'localhost'
port = '5432'

# Save connection details to a file
save_db_config('db_config.txt', db_name, user, password, host, port)

# Insert data from CSV into PostgreSQL
create_table_and_insert_data(csv_file, db_name, user, password, host, port)
