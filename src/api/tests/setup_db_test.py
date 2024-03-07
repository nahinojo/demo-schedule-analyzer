import pytest


@pytest.mark.usefixtures("app_context")
def setup_db_test():
    """
    Tests setup_db function.
    """
    from app.database.setup_db import setup_db
    setup_db()
    return
