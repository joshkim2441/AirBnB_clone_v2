#!/usr/bin/python3
# Starts a Flask web applicaton
import flask
app = flask.Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello hbnb!' """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)