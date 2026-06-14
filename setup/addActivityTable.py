import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS activities (id INTEGER PRIMARY KEY AUTOINCREMENT,
               start_date_local DATETIME,
               distance INTEGER,
               moving_time INTEGER);
               """)

conn.commit()
