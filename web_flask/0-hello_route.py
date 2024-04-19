#!/usr/bin/python3
"""A module for starting flask web Application"""


from flask import Flask

"""Create a Flask application Instance"""
app = Flask(__name__)
"""Route decorator for the Root URL"""


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """When accessing root url, Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """Start the Flask Application on 0.0.0.0:5000"""
    app.run(host='0.0.0.0', port=5000)
