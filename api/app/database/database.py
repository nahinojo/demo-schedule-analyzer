"""
The database class.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.engine import Engine
from app.models import Base
from app.exceptions import DatabaseIsNotInitializedException


class Database:
    """
    The database controller class.
    """
    _engine = None
    _Session = None
    _db_uri = None
    _db_path = None

    @classmethod
    def init(cls, db_uri, db_path) -> None:
        """
        Initializes the database controller class. Must be called before using
        the database.
        """
        if cls._engine is None:
            cls._db_uri = db_uri
            cls._db_path = db_path
            cls._engine = create_engine(cls._db_uri)
            # Ensure all sessions are scoped to local
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
            raise DatabaseIsNotInitializedException(
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

    @classmethod
    def get_db_uri(cls) -> str:
        """
        Returns the database URI.

        Returns
        -------
        str
            The database URI.
        """
        return cls._db_uri

    @classmethod
    def get_db_path(cls) -> str:
        """
        Returns the database path.

        Returns
        -------
        str
            The database path.
        """
        return cls._db_path

    @classmethod
    def end(cls) -> None:
        """
        Closes the database session and engine. Effectively resets
        the Database class
        """
        if cls._engine is None:
            raise DatabaseIsNotInitializedException(
                "Database must be initialized before using the session"
            )
        cls._end_session()
        cls._end_engine()
        os.remove(cls._db_path)
        cls._db_path = None
        cls._db_uri = None
