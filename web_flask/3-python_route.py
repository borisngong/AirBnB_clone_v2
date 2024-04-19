#!/usr/bin/python3
"""A module for starting Flask web Application"""


from flask import Flask


app = Flask(__name__)
"""Creation of the Flask instance"""


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Route decorator for root URL"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route decorator for /hbnb URL"""
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c_app_route(text):
    """Route decorator for /c/<text> URL"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_app_route(text):
    """Route decorator for /python/<text> URL"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    """Start Flask web framework app on 0.0.0.0:5000"""
    app.run(host='0.0.0.0', port=5000)
