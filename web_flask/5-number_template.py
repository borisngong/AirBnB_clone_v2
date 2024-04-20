#!/usr/bin/python3
"""A module for starting Flask web Application"""


from flask import Flask, render_template


app = Flask(__name__)
"""Creation of the Flask instance"""


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_app_route(text):
    """Display “C ” followed by the value of the text variable"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_app_route(text):
    """Display “Python ” followed by the value of the text variable"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_app_route(n):
    """Display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """Start Flask web framework app on 0.0.0.0:5000"""
    app.run(host='0.0.0.0', port=5000)
