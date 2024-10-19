from flask import Flask
from threading import Thread

app_flask = Flask("")

@app_flask.route("/")
def home():
    return "Bot is running!"

def run():
    app_flask.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

