#!/usr/bin/python3
""" Flask framework """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ Displays an HTML page with a list of all
    states
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ displays an html page with info about <id>, if it exists """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """ remove the current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run()
