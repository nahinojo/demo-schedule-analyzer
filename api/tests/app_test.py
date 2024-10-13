"""
Tests application under all configurations.
"""
from flask import Flask


def app_test(app: Flask):
    """
    Tests the creation of the application.
    """
    with app.app_context():
        assert app
