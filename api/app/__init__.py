"""
Initializes the API.
"""
from flask import Flask
from flask_cors import CORS

from app.config import Config  # Must be first import.


def create_app():
    """
    Creates the Flask app.
    """
    app = Flask(__name__)
    app.config.from_object(Config.get_config())
    CORS(app)
    return app
