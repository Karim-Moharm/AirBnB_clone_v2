#!/usr/bin/python3
"""script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """close the session after fetching the data
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_states_data():
    """display List of states
    """
    state_values = storage.all(State).values()
    return render_template('8-cities_by_states.html',
                           state_values=state_values, title='HBNB')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
