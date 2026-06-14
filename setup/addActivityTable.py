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

cursor.execute("""
                INSERT INTO activities (start_date_local, distance, moving_time)
               VALUES ("2018-02-16T06:52:54Z", 28099, 4207)
               """)

conn.commit()
