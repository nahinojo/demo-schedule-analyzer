"""
Utility function for clearing the database.
"""
from .session_scope import session_scope
from app.models import Base


def empty_db():
    """
    Removes all entries in the database without deleting the tables.
    """
    with session_scope() as session:
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()
