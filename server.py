from flask import Flask
from threading import Thread


app = Flask('')

@app.route("/")
def main():
  return "Always Online Self-Bot On!"


def run():
  app.run(host="0.0.0.0",port=8080)


def deploy():
  server = Thread(target=run)
  server.start()
