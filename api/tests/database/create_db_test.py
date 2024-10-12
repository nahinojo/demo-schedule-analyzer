"""
Tests the creation of the database.
"""
import pytest


@pytest.mark.usefixtures("app_context")
def create_db_test():
    """
    Tests setup_db function.
    """

    from app.database import Base, Session
    from app.database.create_db import create_db
    create_db()
    with Session() as session:
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()
