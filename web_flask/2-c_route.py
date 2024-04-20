#!/usr/bin/python3
""" Flask framework """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ returns 'Hello HBNB' """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ return 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text():
    """returns text given """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    """ Start the flask development server """
    app.run()
