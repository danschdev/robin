#!/usr/bin/env python3
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1", temperature=0)

messages = [
    (
        "system",
        "Du bist ein hilfreicher Assistent der meine Sport-Leistungsdaten mit mir bespricht. Sie kommen im Format (Zeitpunkt, Strecke in Metern, Zeit in Sekunden). Wie haben sich meine Leistungen in Ende Mai und Anfang/Mitte Juni entwickelt? Bedenke, dass längere Strecken natürlich mehr Zeit brauchen und versuche, Durchschnittstempos zu berechnen",
    ),
    ("human", "(2026-06-14T08:16:00Z, 6360, 2360)"),
    ("human", "(2026-06-11T08:17:00Z, 14130, 5220"),
    ("human", "(2026-06-09T08:40:00Z, 12790, 4740)"),
    ("human", "(2026-06-07T06:08:00Z, 6530, 2802"),
    ("human", "(2026-06-03T05:59:00Z, 3530, 1324)"),
    ("human", "(2026-05-28T17:18:00Z, 7140, 2669)"),
    ("human", "(2026-05-26T06:11:00Z, 7870, 2577)"),
    ("human", "(2026-05-24T08:06:00Z, 5720, 2262)"),
    ("human", "(2026-05-21T05:28:00Z, 7530, 2866)"),
    ("human", "(2026-05-16T07:31:00Z, 6290, 2377)"),
    ("human", "(2026-05-12T10:02:00Z, 10280, 4080)"),
    ("human", "(2026-05-10T15:57:00Z, 5440, 2014)"),
    ("human", "(2026-05-08T11:17:00Z, 10320, 3724)"),
    ("human", "(2026-05-01T08:27:00Z, 8810, 3263)"),
    ("human", "(2026-04-26T07:18:00Z, 3010, 1087)"),
    ("human", "(2026-04-22T07:41:00Z, 6910, 2875)"),
]

ai_msg = llm.invoke(messages)

print(ai_msg.content)
