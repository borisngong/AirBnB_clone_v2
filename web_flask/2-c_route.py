#!/usr/bin/python3
"""A module for starting Flask web application"""


from flask import Flask


app = Flask(__name__)
"""This creates a Flask application instance"""


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Route decorator for route URL"""
    return "Hello HNBN!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route Decorator for /hbnb URL"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_app_route(text):
    """Route decorator for /c/<text> URL"""
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    """Start flasks application on 0.0.0.0:5000"""
    app.run(host='0.0.0.0', port=5000)
