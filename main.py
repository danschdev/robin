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
                INSERT INTO requests (content)
               VALUES (?)
               RETURNING id, content
             """
data = [requestText]

response = cursor.execute(statement, data)

requestId, requestText = response.fetchone()
conn.commit()

url = "http://localhost:11434/api/chat"
thinkParameter = False
data = {
    "model": "gemma3:1b",
    "messages": [
        {
            "role": "user",
            "content": requestText,
        }
    ],
    "think": thinkParameter,
}
with requests.post(url, data=json.dumps(data), stream=True) as stream:
    responseThoughts = ""
    responseText = ""
    finishedThinking = False
    for line in stream.iter_lines():
        object = json.loads(line)
        message = object.get("message")
        if message and thinkParameter and "thinking" in message:
            responseThoughts += object["message"]["thinking"]
            print(object["message"]["thinking"], end="")
        else:
            if thinkParameter and not finishedThinking:
                finishedThinking = True
                print("\n\n------------------------\n\n")
            if message and message["role"] == "assistant":
                responseText += object["message"]["content"]
                if responseText:
                    print(object["message"]["content"], end="")

statement = """
               INSERT INTO responses (content, request_id)
               VALUES (?, ?)
               """
data = [responseText, requestId]

cursor.execute(statement, data)


conn.commit()
