"""
The database class.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.engine import Engine
from flask import current_app

from app.models import Base
from app.exceptions import DatabaseNotInitializedException
from app.utils.calendar import extract_courses_from_calendar


class Database:
    """
    The database controller class.
    """
    _engine = None
    _Session = None

    @classmethod
    def init(cls) -> None:
        """
        Initializes the database controller class. Must be called before using
        the database.
        """
        # Ensure new database file is created.
        if current_app.config["APP_ENV"] != "testing":
            db_path = current_app.config["DATABASE_PATH"]
            if os.path.isfile(db_path):
                os.remove(db_path)
            with open(db_path, "w+") as f:
                f.write("")

        if cls._engine is None:
            db_uri = current_app.config["DATABASE_URI"]
            cls._engine = create_engine(db_uri)
        Base.metadata.create_all(Database.get_engine())
        cls._Session = scoped_session(sessionmaker(bind=cls._engine))
        return

    @classmethod
    def get_engine(cls) -> Engine:
        """
        Returns the database engine.

        Returns
        -------
        Engine
            The database engine.
        """
        if not cls._engine:
            raise DatabaseNotInitializedException(
                "Database must be initialized before using the engine"
            )
        return cls._engine

    @classmethod
    def _end_engine(cls) -> None:
        """
        Disposes and removes the database engine.
        """
        engine = cls.get_engine()
        Base.metadata.drop_all(engine)
        engine.dispose()
        cls._engine = None

    @classmethod
    def get_session(cls) -> Session:
        """
        Returns the database session.

        Returns
        -------
        Session
            The database session.
        """
        if cls._Session is None:
            raise DatabaseNotInitializedException(
                "Database must be initialized before using the session"
            )
        return cls._Session

    @classmethod
    def commit_session(cls) -> None:
        """
        Commits the database session.
        """
        if cls._Session is None:
            raise DatabaseNotInitializedException(
                "Database must be initialized before using the session"
            )
        _session = cls.get_session()
        try:
            _session.commit()
        except Exception as e:
            _session.rollback()
            raise e
        finally:
            _session.close()

    @classmethod
    def empty_db(cls) -> None:
        """
        Empties the database.
        """
        with cls.get_session() as session:
            for table in Base.metadata.sorted_tables:
                session.execute(table.delete())
            cls.commit_session()

    @classmethod
    def _create_db_file(cls):
        """
        Deletes the database at the path.
        """
        if current_app.config["APP_ENV"] != "testing":
            db_path = current_app.config["DATABASE_PATH"]
            if os.path.isfile(db_path):
                os.remove(db_path)
            with open(db_path, "w+") as f:
                f.write("")
        else:
            raise Exception("Cannot delete database in testing environment")

    @classmethod
    def update_db_from_calendar(cls) -> None:
        """
        Overwrites the database with current demo calendar data.
        """
        cls.empty_db()
        with cls.get_session() as session:
            all_courses = extract_courses_from_calendar()
            for course in all_courses:
                session.add(course)
