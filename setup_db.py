import sqlite3
import os

DB_FILE = 'database.db'
SCHEMA_FILE = 'schema.sql'

def setup_database():
    if os.path.exists(DB_FILE):
        print(f"Removing existing {DB_FILE}...")
        os.remove(DB_FILE)
    
    print(f"Creating new {DB_FILE} and executing {SCHEMA_FILE}...")
    
    with sqlite3.connect(DB_FILE) as conn:
        with open(SCHEMA_FILE, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        # Execute the schema script
        conn.executescript(sql_script)
        
    print("Database setup completed.")
    

if __name__ == "__main__":
    setup_database()
