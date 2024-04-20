#!/usr/bin/python3
""" Flask framework """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ returns 'Hello Hbnb' """
    return "Hello HBNB!"


@app.route("/HBNB", strict_slashes=False)
def HBNB():
    """ returns 'HBNB' """
    return "NBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """ returns text given """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={'text': 'is cool'})
@app.route("/python/text", strict_slashes=False)
def display(text):
    """ display 'python' followed by the
    value of the text
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    """ Start the flask development server """
    app.run()
