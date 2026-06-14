from flask import Flask
from pandas import pandas
from pathlib import Path
import sqlite3

app = Flask(__name__)


@app.route("/")
def hallo():
    return "Hallo Flask"


@app.route("/chat")
def getChat():
    script_directory = Path(__file__).resolve().parent.parent

    print(script_directory)
    db = script_directory / "data" / "database.db"
    conn = sqlite3.connect(db)

    statement = """
                    SELECT created_at, role, content FROM messages
                    ORDER BY created_at ASC
                """

    df = pandas.read_sql_query(statement, conn)

    output = ""

    for row in df.iterrows():
        output += str("<b>" + row[1]["role"] + "</b>: " + row[1]["content"] + "<br/>")

    return output
