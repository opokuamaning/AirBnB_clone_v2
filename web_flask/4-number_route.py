#!/usr/bin/python3
"""
    Start a Flask web application
    lisen on 0.o.o.o, port 5000
    route (/) display "Hello HBNB!
"""

from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)