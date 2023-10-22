#!/usr/bin/python3
"""script that starts a Flask web application
"""
from models.state import State
from models import storage
from flask import Flask, render_template
import sys
sys.path.append('..')

app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """close the session after fetching the data
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states_data():
    """display List of states
    """
    state_values = storage.all(State).values()
    return render_template('7-states_list.html',
                           state_values=state_values, title='HBNB')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
