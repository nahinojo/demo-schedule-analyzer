"""
The database class.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.models import Base


class Database:
    """
    The database controller class.
    """
    _engine = None
    _Session = None

    @classmethod
    def init(cls, db_url):
        """
        Initializes the database controller class. Must be called before using
        the database.
        """
        if cls._engine is None:
            cls._engine = create_engine(db_url)
            # Ensure all sessions are scoped to local
            cls._Session = scoped_session(sessionmaker(bind=cls._engine))

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
    def get_session(cls):
        """
        Returns the database session.

        Returns
        -------
        Session
            The database session.
        """
        if cls._Session is None:
            raise Exception("Database not initialized")
        return cls._Session

    @classmethod
    def commit_session(cls):
        """
        Commits the database session.
        """
        session = cls.get_session()
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def remove_session(cls):
        """
        Removes the database session.
        """
        session = cls.get_session()
        session.remove()
