#!/usr/bin/env python3
import json
import requests

requestText = "Moin! Schön dass du lokal auf meinem Rechner läufst und über die API ansprechbar bist. Gib mir mal einen Text aus zwei Absätzen, der dich etwas Denkvermögen kostet."
url = "http://localhost:11434/api/chat"
data = {
    "model": "gpt-oss:20b",
    "messages": [
        {
            "role": "user",
            "content": requestText,
        }
    ],
}
print(requestText)
with requests.post(url, json.dumps(data), stream=True) as stream:
    responseText = ""
    for line in stream.iter_lines():
        object = json.loads(line)
        if object["message"] and object["message"]["role"] == "assistant":
            responseText += object["message"]["content"]
            if responseText:
                print(object["message"]["content"], end="")
