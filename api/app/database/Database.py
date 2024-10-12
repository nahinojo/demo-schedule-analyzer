"""
The database class.
"""
from app.database import engine, Session
from app.models import Base
from app.utils.calendar import extract_courses_from_calendar


class Database:
    """
    The database class.
    """

    def __init__(self):
        self.engine = engine
        self.Session = Session

    def clear_all(self):
        """
        Removes all entries in the database without deleting the tables.
        """
        with self.Session() as session:
            for table in reversed(Base.metadata.sorted_tables):
                session.execute(table.delete())
            session.commit()

    def fill_from_calendar(self):
        """
        Updates the database with current demo calendar data.
        """
        self.clear_all()
        with self.Session() as session:
            all_courses = extract_courses_from_calendar()
            for course in all_courses:
                session.add(course)
            session.commit()
