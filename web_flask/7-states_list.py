#!/usr/bin/python3
""" Flask framework """
from models import storage
from flask import Flask, render_template
from models.state import State
from os import environ

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """ remove the current SQLAlchemy session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Displays an HTML page with a list of all
    state objects in DBStorage
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
