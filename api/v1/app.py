#!/usr/bin/python3
""" Runs api routes """

from flask import Flask, jsonify
from flask_cors import CORS

from models import storage
from api.v1.views app_views

from os import getenv

app = Flask(__name__)
CORS(app, resources=r"/*", origins="0.0.0.0")

app.regester_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(e):
    storage.close()


if __name__ == "__main__":
    HOST = getenv("HBNB_API_HOST") or "0.0.0.0"
    PORT = getenv("HBNB_API_PORT") or 5000
    app.run(HOST, int(PORT), threaded=True)
