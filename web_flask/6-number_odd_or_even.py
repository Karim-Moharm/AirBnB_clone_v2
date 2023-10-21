#!/usr/bin/python3
"""script that starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """route function that displays Hello HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """route function that displays HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """route function that displays C followed by some text
    """
    return f"C {text}".replace("_", " ")


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def display_python(text="is cool"):
    """route function that displays Python followed by some text
    """
    return f"Python {text}".replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """display n is a number only if n is an integer
    """
    if type(n) is int:
        return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """display a HTML page only if n is an integer
    """
    if type(n) is int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """display a HTML page only if n is an integer
    """
    if type(n) is int:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
