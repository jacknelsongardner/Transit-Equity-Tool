import psycopg2
import csv
import random


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

        # Drop table if it exists
        cur.execute("""
        DROP TABLE IF EXISTS geo_info;
        """)
        conn.commit()

        # Create geo_info table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS geo_info (
            ID_Year TEXT,
            Year TEXT,
            ID_Race TEXT,
            Race TEXT,
            Household_Income_by_Race TEXT,
            Household_Income_by_Race_Moe TEXT,
            avg_cars_per_person TEXT, 
            avg_persons_per_household TEXT,
            Geography TEXT,
            ID_Geography TEXT,
            PRIMARY KEY (ID_Geography, ID_Year, ID_Race)
        );
        """)
        conn.commit()

        # Insert data into geo_info from CSV
        with open(stops_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ID_Year = row['ID Year']
                Year = row['Year']  # Updated to match column name
                ID_Race = row['ID Race']
                Race = row['Race']
                household_income = row['Household Income by Race']
                household_income_race_moe = row['Household Income by Race Moe']
                # placeholder
                avg_cars_per_person = random.uniform(0, 2)
                # placeholder
                avg_persons_per_household = random.uniform(1, 6)
                geography = row['Geography']
                id_geography = row['ID Geography']

                cur.execute("""
                INSERT INTO geo_info (ID_Year, Year, ID_Race, Race, Household_Income_by_Race, Household_Income_by_Race_Moe, avg_cars_per_person, avg_persons_per_household, Geography, ID_Geography)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (ID_Geography, ID_Year, ID_Race) DO NOTHING;
                """, (ID_Year, Year, ID_Race, Race, household_income, household_income_race_moe, avg_cars_per_person, avg_persons_per_household, geography, id_geography))

        conn.commit()
        cur.close()
        conn.close()
        print("Data inserted successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Usage
stops_csv = 'income by location.csv'  # Your CSV file path
db_name = 'demographic_info'
user = 'jack'
password = 'xfiles'
host = 'localhost'
port = '5432'

# Insert data from CSV into PostgreSQL
create_tables_and_insert_data(stops_csv, db_name, user, password, host, port)
