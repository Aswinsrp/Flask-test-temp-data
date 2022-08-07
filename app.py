from flask import Flask, Response, Request
from pymongo import MongoClient
from datetime import datetime, timedelta
import os
import waitress


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome"

@app.route("/health", methods=["GET"])
def getHealth():
    return "Application started successfully"

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get('PORT',33507))
    waitress.serve(app, port=port)
    