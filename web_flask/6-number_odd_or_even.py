#!/usr/bin/python3
"""
    Start a Flask web application
    lisen on 0.o.o.o, port 5000
    route (/) display "Hello HBNB!
"""

from flask import Flask, render_template
app.url_map.strict_slashes = False
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display text"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display text"""
    return "C {}".format(text.replace("_", " "))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """display text"""
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display text"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display text"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display text"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, odd_or_even="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, odd_or_even="odd")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)