#!/usr/bin/python3
""" Flask framework """
from models.amenity import Amenity
from models.state import State
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    """ HBNB filters """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    return render_template('10-hbnb_filters.html',
                           states=st_ct,
                           amenities=amenities)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
