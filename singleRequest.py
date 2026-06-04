#!/usr/bin/env python3
import json
import requests

models = ["gemma3:1b", "gpt-oss:20b", "llama3.1", "qwen2"]
requestText = "Analysiere die folgende Benutzeranfrage und entscheide, welches Tool verwendet werden soll: Kalender, Wetter, Suche oder E-Mail. Antworte nur mit dem Toolnamen."
prefaceText = "Hallo, ich habe folgende Anfrage erhalten. Bitte entscheide für mich, welches Sprachmodell für diese am besten geeignet ist, begründe nicht und nenne die anderen nicht in deiner Antwort:"
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
print(prefaceText + requestText)
with requests.post(url, data=json.dumps(data), stream=True) as stream:
    responseThoughts = ""
    responseText = ""
    finishedThinking = False
    for line in stream.iter_lines():
        object = json.loads(line)
        message = object.get("message")
        if message and message["role"] == "assistant":
            responseText += object["message"]["content"]
    for model in models:
        print(model in responseText)
        if model.upper() in responseText.upper():
            print(model)
            print(model.upper())
    print(responseText)
