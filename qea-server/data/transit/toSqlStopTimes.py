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
        DROP TABLE IF EXISTS transit_stop_times;
        """)
        conn.commit()

        # Create stops_routes table to associate stops with routes
        cur.execute("""
        CREATE TABLE IF NOT EXISTS transit_stop_times (
            trip_id TEXT,
            stop_id TEXT,
            arrival_time TEXT,
            departure_time TEXT,
            stop_sequence TEXT,
            PRIMARY KEY (trip_id, stop_id),
            
            FOREIGN KEY (stop_id) REFERENCES transit_stops(stop_id)

        );
        """)
        conn.commit()

        # Insert data into transit_stops from stops CSV
        with open(stops_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                trip_id = row['trip_id']
                stop_id = row['stop_id']
                arrival_time = row['arrival_time']
                departure_time = row['departure_time']
                stop_sequence = row['stop_sequence']

                cur.execute("""
                INSERT INTO transit_stop_times (trip_id, stop_id, arrival_time, departure_time, stop_sequence)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (trip_id, stop_id) DO NOTHING;
                """, (trip_id, stop_id, arrival_time, departure_time, stop_sequence))


        conn.commit()
        cur.close()
        conn.close()
        print("Data inserted successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Usage
stops_csv = 'stop_times.csv'  # Your stops CSV file path
routes_csv = 'routes_data.csv'  # Your routes CSV file path
trips_csv = 'trips_data.csv'  # Your trips CSV file path
db_name = 'transit_db'
user = 'jack'
password = 'xfiles'
host = 'localhost'
port = '5432'

# Insert data from CSVs into PostgreSQL
create_tables_and_insert_data(stops_csv, db_name, user, password, host, port)
