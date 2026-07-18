import pandas as pd
import sqlite3
import os

# File paths
CSV_FILE = "data/SampleSuperstore.csv"
DB_FILE = "database/sales.db"

def create_database():
    try:
        # Read the CSV
        df = pd.read_csv(CSV_FILE, encoding="latin1")

        # Create database folder if it doesn't exist
        os.makedirs("database", exist_ok=True)

        # Connect to SQLite
        conn = sqlite3.connect(DB_FILE)

        # Store data in SQLite
        df.to_sql("sales", conn, if_exists="replace", index=False)

        conn.close()

        print("✅ Database created successfully!")
        print(f"Total Records: {len(df)}")
        print(f"Total Columns: {len(df.columns)}")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    create_database()