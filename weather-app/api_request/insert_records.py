import os
from api_request import mock_fetch_data
import psycopg2
from dotenv import load_dotenv
load_dotenv()


def connect_to_db(): 
    print("Connecting to the Postgres database...")
    try: 
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "db"), 
            port=os.getenv("POSTGRES_PORT", 5432), 
            dbname="postgres", 
            user="postgres", 
            password="postgres"
        )
        return conn
    except psycopg2.Error as e: 
        print(f"Database connection failed: {e}")
        raise

def create_table(conn): 
    print("Creating table if not exist...")
    try: 
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev; 
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data(
                city TEXT, 
                temperature FLOAT, 
                weather_description TEXT, 
                wind_speed FLOAT, 
                time TIMESTAMP, 
                inserted_at TIMESTAMP DEFAULT NOW(), 
                utc_offset TEXT
            )
        """)
        conn.commit()
        print("Table dev created successfully")
    except psycopg2.Error as e: 
        print(f"Failed to create table : {e}")
        raise 

def insert_record(conn, data): 
    print("Inserting data to database...")
    try : 
        weather = data["current"]
        location = data["location"]
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO dev.raw_weather_data (
         city, 
         temperature, 
         weather_description, 
         wind_speed, 
         time, 
         inserted_at, 
         utc_offset
        ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)             
        """, (
            location["name"], 
            weather["temperature"], 
            weather["weather_descriptions"][0], 
            weather["wind_speed"], 
            location["localtime"], 
            location["utc_offset"]
        ))
        conn.commit()
        print("Data successfully added to db.")
    except psycopg2.Error as e :
        print(f"Error inserting data in the db : {e}")
        
def main(): 
    try:
        data = mock_fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_record(conn, data)
    except Exception as e: 
        print(f"An error occured during execution: {e}")
    finally: 
        if 'conn' in locals(): 
            conn.close()
            print("Database connection closed.")

main()