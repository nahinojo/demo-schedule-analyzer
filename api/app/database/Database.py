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

    @classmethod
    def init(cls):
        """
        Initializes the database.
        """
        cls.engine = engine
        cls.Session = Session

    @classmethod
    def clear_all(cls):
        """
        Removes all entries in the database without deleting the tables.
        """
        with cls.Session() as session:
            for table in reversed(Base.metadata.sorted_tables):
                session.execute(table.delete())
            session.commit()

    @classmethod
    def fill_from_calendar(cls):
        """
        Updates the database with current demo calendar data.
        """
        cls.clear_all()
        with cls.Session() as session:
            all_courses = extract_courses_from_calendar()
            for course in all_courses:
                session.add(course)
            session.commit()
