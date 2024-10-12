"""
Tests the creation of the app.
"""
import pytest


@pytest.mark.usefixtures("app_context")
def create_app_test():
    """
    Tests the creation of the app with no data added to the database.
    """
    assert True
