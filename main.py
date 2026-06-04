#!/usr/bin/env python3
import json
from pathlib import Path
import requests
import sqlite3

script_directory = Path(__file__).resolve().parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

print("Enter request: ")
requestText = input()

statement = """
                INSERT INTO messages (content, role)
               VALUES (?,  "user")
             """

cursor.execute(statement, [requestText])
conn.commit()

url = "http://localhost:11434/api/chat"
data = {
    "model": "gemma3:1b",
    "messages": [
        {
            "role": "user",
            "content": requestText,
        }
    ],
}
with requests.post(url, data=json.dumps(data), stream=True) as stream:
    responseThoughts = ""
    responseText = ""
    for line in stream.iter_lines():
        object = json.loads(line)
        message = object.get("message")
        responseText += object["message"]["content"]
        if responseText:
            print(object["message"]["content"], end="")

statement = """
               INSERT INTO messages (content, role)
               VALUES (?, "assistant")
               """
data = [responseText]

cursor.execute(statement, data)


conn.commit()
