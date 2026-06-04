import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS requests (id INTEGER PRIMARY KEY AUTOINCREMENT,
               content TEXT NOT NULL);
               """)
cursor.execute("""
               CREATE TABLE IF NOT EXISTS responses (id INTEGER PRIMARY KEY AUTOINCREMENT,
               content TEXT NOT NULL,
               request_id INTEGER,
               CONSTRAINT fk_requests
               FOREIGN KEY (request_id)
               REFERENCES requests(id))
               """)
conn.close()
