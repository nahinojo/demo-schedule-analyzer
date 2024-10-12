"""
Clears all entries in the database.
"""

from app.database import Session, Base


def clear_db():
    """
    Removes all entries in the database without deleting the tables.
    """
    with Session() as session:
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()
    return
