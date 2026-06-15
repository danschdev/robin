import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

secondsPerMinute = 60

activities = [
    ("2026-06-14T08:16:00Z", 6360, 39 * secondsPerMinute + 20),
    ("2026-06-11T08:17:00Z", 14130, (60 + 27) * secondsPerMinute),
    ("2026-06-09T08:40:00Z", 12790, (60 + 19) * secondsPerMinute),
    ("2026-06-07T06:08:00Z", 6530, 46 * secondsPerMinute + 42),
    ("2026-06-03T05:59:00Z", 3530, 22 * secondsPerMinute + 4),
    ("2026-05-28T17:18:00Z", 7140, 44 * secondsPerMinute + 29),
    ("2026-05-26T06:11:00Z", 7870, 42 * secondsPerMinute + 57),
    ("2026-05-24T08:06:00Z", 5720, 37 * secondsPerMinute + 42),
    ("2026-05-21T05:28:00Z", 7530, 47 * secondsPerMinute + 46),
    ("2026-05-16T07:31:00Z", 6290, 39 * secondsPerMinute + 37),
    ("2026-05-12T10:02:00Z", 10280, (60 + 8) * secondsPerMinute),
    ("2026-05-10T15:57:00Z", 5440, 33 * secondsPerMinute + 34),
    ("2026-05-08T11:17:00Z", 10320, (60 + 2) * secondsPerMinute + 4),
    ("2026-05-01T08:27:00Z", 8810, 54 * secondsPerMinute + 23),
    ("2026-04-26T07:18:00Z", 3010, 18 * secondsPerMinute + 7),
    ("2026-04-22T07:41:00Z", 6910, 47 * secondsPerMinute + 55),
]

cursor.executemany(
    """
                INSERT INTO activities (start_date_local, distance, moving_time)
               VALUES (?, ?, ?)
               """,
    activities,
)

conn.commit()
