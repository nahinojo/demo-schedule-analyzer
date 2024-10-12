"""
Tests the initialization of the database.
"""
import pytest


@pytest.mark.usefixtures("app_context_with_real_data")
def create_db_test():
    """
    Tests the creation of the database and if it can be populated with real
    data.
    """
    # TODO: Test if there is indeed real data inside the database.
    return
