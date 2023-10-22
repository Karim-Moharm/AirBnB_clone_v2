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


@app.route('/states/', strict_slashes=False)
def states_list():
    """
    Template html Cities
    """
    state_values = storage.all(State).values()
    return render_template('7-states_list.html',
                           state_values=state_values, title='HBNB')


@app.route('/states/<id>', strict_slashes=False)
def cities_states_list(id):
    wanted_state = storage.all(State)
    state_id = 'State.{}'.format(id)
    if state_id in wanted_state:
        wanted_state = wanted_state[state_id]
    else:
        wanted_state = None
    return render_template('9-states.html',
                           my_states=wanted_state,
                           title='HBNB')
