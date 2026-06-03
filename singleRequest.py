#!/usr/bin/env python3
import json
import requests

requestText = "Hallo, lass uns ein bisschen plaudern!"
prefaceText = "Hallo, ich habe folgende Anfrage erhalten. Bitte entscheide für mich, welches Sprachmodell diese am schnellsten und ressourcenschonendsten löst und gib mir nur den exakten Namen des Modells zurück, wie es in folgender Liste steht:"
prefaceText += "gemma3:1b, gpt-oss:20b, llama3.1, qwen2; Hier die Anfrage: "
url = "http://localhost:11434/api/chat"
data = {
    "model": "gemma3:1b",
    "messages": [
        {
            "role": "user",
            "content": prefaceText + requestText,
        }
    ],
}
print(requestText)
with requests.post(url, data=json.dumps(data), stream=True) as stream:
    responseThoughts = ""
    responseText = ""
    finishedThinking = False
    for line in stream.iter_lines():
        object = json.loads(line)
        message = object.get("message")
        if message and message["role"] == "assistant":
            responseText += object["message"]["content"]
            if responseText:
                print(object["message"]["content"], end="")
