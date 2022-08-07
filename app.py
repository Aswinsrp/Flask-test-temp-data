from flask import Flask, Response, Request
from pymongo import MongoClient
from datetime import datetime, timedelta


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome"

@app.route("/health", methods=["GET"])
def getHealth():
    return "Application started successfully"

if __name__ == "__main__":
    app.run(debug=True)