import psycopg2
import csv

# Function to create tables and insert data
def create_tables_and_insert_data(stops_csv, db_name, user, password, host, port):
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
        DROP TABLE IF EXISTS transit_trips;
        """)
        conn.commit()

        # Create stops_routes table to associate stops with routes
        cur.execute("""
        CREATE TABLE IF NOT EXISTS transit_trips (
            trip_id TEXT,
            route_id TEXT,
            
            
            
            PRIMARY KEY (trip_id, route_id),
            
            FOREIGN KEY (route_id) REFERENCES transit_routes(route_id)

        );
        """)
        conn.commit()

        # Insert data into transit_stops from stops CSV
        with open(stops_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                trip_id = row['trip_id']
                route_id = row['route_id']

                cur.execute("""
                INSERT INTO transit_trips (trip_id, route_id)
                VALUES (%s, %s)
                ON CONFLICT (trip_id, route_id) DO NOTHING;
                """, (trip_id, route_id))


        conn.commit()
        cur.close()
        conn.close()
        print("Data inserted successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Usage
stops_csv = 'trips.csv'  # Your stops CSV file path
db_name = 'transit_db'
user = 'jack'
password = 'xfiles'
host = 'localhost'
port = '5432'

# Insert data from CSVs into PostgreSQL
create_tables_and_insert_data(stops_csv, db_name, user, password, host, port)
