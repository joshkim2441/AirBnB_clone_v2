#!/usr/bin/python3
""" Flask framework """
from flask import Flask
from flask import render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """ print n is a number """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ dispalys an HTML page only if n is an integer """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_n(n):
    """ displays an HTML page only if n is an integer """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run()
