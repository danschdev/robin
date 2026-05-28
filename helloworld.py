#!/usr/bin/env python3
import json
import requests

url = "http://localhost:11434/api/chat"
data = {
    "model": "gpt-oss:20b",
    "messages": [
        {
            "role": "user",
            "content": "Moin, schön dass du lokal auf meinem Rechner läufst und über die API ansprechbar bist.",
        }
    ],
}

with requests.post(url, json.dumps(data)) as stream:
    responseText = ""
    for line in stream.iter_lines():
        object = json.loads(line)
        if object["message"] and object["message"]["role"] == "assistant":
            responseText += object["message"]["content"]

print(responseText)
