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
        DROP TABLE IF EXISTS transit_stops;
        """)
        conn.commit()

        # Create table with a composite primary key
        cur.execute("""
        CREATE TABLE IF NOT EXISTS transit_stops (
            stop_id TEXT PRIMARY KEY,
            stop_code TEXT,
            stop_name TEXT,
            stop_lat FLOAT,
            stop_lon FLOAT
        );
        """)
        conn.commit()

         # Create table with a composite primary key
        

        # Read the CSV and insert data
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                stop_id = row['stop_id']
                stop_code = row['stop_code']
                stop_name = row['stop_name']
                stop_lat = float(row['stop_lat'])
                stop_lon = float(row['stop_lon'])

                if stop_code != '' and stop_id != '' and stop_name != '':

                    cur.execute("""
                    INSERT INTO transit_stops (stop_id, stop_code, stop_name, stop_lat, stop_lon)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (stop_id) DO NOTHING;
                    """, (stop_id, stop_code, stop_name, stop_lat, stop_lon))

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
csv_file = 'stops.csv'  # Your CSV file path
db_name = 'transit_db'
user = 'jack'
password = 'xfiles'
host = 'localhost'
port = '5432'

# Save connection details to a file
save_db_config('db_config.txt', db_name, user, password, host, port)

# Insert data from CSV into PostgreSQL
create_table_and_insert_data(csv_file, db_name, user, password, host, port)
