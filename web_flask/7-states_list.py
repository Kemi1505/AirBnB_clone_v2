#!/usr/bin/python3
"""
Module: Flask States App
Description: This module initializes a Flask web application that displays a list of states 
from a storage system in alphabetical order. The states are fetched from a storage backend 
and passed to an HTML template for rendering.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

# Initialize Flask application
app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def display_states():
    """
    Route: /states_list
    Method: GET
    Description: Displays a list of states in alphabetical order.
    Fetches all state objects from the storage and passes them to the template.
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(self):
    """
    Teardown Method
    Description: Closes the storage after each request to free up resources.
    """
    storage.close()

if __name__ == "__main__":
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
