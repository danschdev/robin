#!/usr/bin/env python3
import json
import requests

requestText = "Guten Morgen Sonnenschein, weck mich auf und komm herein!"
url = "http://localhost:11434/api/chat"
data = {
    "model": "gpt-oss:20b",
    "messages": [
        {
            "role": "user",
            "content": requestText,
        }
    ],
    "think": True,
}
print(requestText)
with requests.post(url, data=json.dumps(data), stream=True) as stream:
    responseThoughts = ""
    responseText = ""
    finishedThinking = False
    for line in stream.iter_lines():
        object = json.loads(line)
        message = object.get("message")
        if message and "thinking" in message:
            responseThoughts += object["message"]["thinking"]
            print(object["message"]["thinking"], end="")
        else:
            if not finishedThinking:
                finishedThinking = True
                print("\n\n------------------------\n\n")
            if message and message["role"] == "assistant":
                responseText += object["message"]["content"]
                if responseText:
                    print(object["message"]["content"], end="")
