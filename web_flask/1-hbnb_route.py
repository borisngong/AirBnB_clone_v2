#!/usr/bin/python3
"""A module for starting Flask web application"""

from flask import Flask

app = Flask(__name__)
"""Create a Flask application instance"""


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Route decorator for the root URL"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route decorator for the '/hbnb' URL"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
