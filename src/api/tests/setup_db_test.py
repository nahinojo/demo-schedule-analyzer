import pytest


@pytest.mark.usefixtures("app_context")
def setup_db_test():
    """
    Tests setup_db function.
    """
    from app.database.setup import setup
    setup()
