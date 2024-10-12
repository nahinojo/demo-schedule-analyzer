"""
Utility function for managing database sessions.
"""
from contextlib import contextmanager

from app.database.database import Database


@contextmanager
def session_scope():
    """
    Returns a database session scoped to the current request. Handles
    """
    session = Database.get_session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
