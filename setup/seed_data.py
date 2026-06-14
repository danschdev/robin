import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

activities = [
    ("2026-06-14T08:16:00Z", 6360, 39 * 60 + 20),
    ("2026-06-11T08:17:00Z", 14130, (60 + 27) * 60),
    ("2026-06-09T08:40:00Z", 12790, (60 + 19) * 60),
]

cursor.executemany(
    """
                INSERT INTO activities (start_date_local, distance, moving_time)
               VALUES (?, ?, ?)
               """,
    activities,
)

conn.commit()
