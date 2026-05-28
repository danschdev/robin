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

req = requests.post(url, json.dumps(data))
print(req.status_code)
