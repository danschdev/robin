#!/usr/bin/env python3
import json
import requests

print("Enter request: ")
requestText = input()
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
