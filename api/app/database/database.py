"""
The database class.
"""
from app.models import Base


class Database:
    """
    The database class.
    """
    _engine = None

    @classmethod
    def init(cls, engine):
        """
        Initializes the database.
        """
        cls._engine = engine

    @classmethod
    def get_engine(cls):
        """
        Returns the database engine.

        Returns
        -------
        Engine
            The database engine.
        """
        return cls._engine

    @classmethod
    def Session(cls):
        """
        Returns the database session.

        Returns
        -------
        Session
            The database session.
        """
        from sqlalchemy.orm import sessionmaker
        engine = cls.get_engine()
        return sessionmaker(bind=engine)

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
        from app.utils.calendar import extract_courses_from_calendar
        cls.clear_all()
        with cls.Session() as session:
            all_courses = extract_courses_from_calendar()
            for course in all_courses:
                session.add(course)
            session.commit()
