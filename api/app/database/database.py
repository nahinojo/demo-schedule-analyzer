"""
The database class.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.engine import Engine
from flask import current_app

from app.models import Base
from app.exceptions import DatabaseNotInitializedException


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
        if cls._engine is None:
            db_uri = current_app.config["DATABASE_URI"]
            cls._engine = create_engine(db_uri)
            # Ensure all sessions are scoped to local thread.
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
        _session = cls.get_session()
        try:
            _session.commit()
        except Exception as e:
            _session.rollback()
            raise e
        finally:
            _session.close()

    @classmethod
    def _end_session(cls) -> None:
        """
        Closes and removes the database session.
        """
        _session = cls.get_session()
        _session.close()
        cls._Session = None
