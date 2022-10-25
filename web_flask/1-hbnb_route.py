#!/usr/bin/python3
""" Runs a Flask web Application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Return hello hbnb"""
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string to the root route /hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0"
