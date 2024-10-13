"""
Demo DAO.
"""
from sqlalchemy.orm import Session
from app.models import Demo
from ._base_dao import _BaseDAO


class DemoDAO(_BaseDAO):
    """
    Demo Data Access Object (DAO).
    """

    @staticmethod
    def get_by_id(session: Session,
                  demo_id: int,
                  **kwargs
                  ) -> Demo | None:
        """
        Retrieves a demo from the database.

        Parameters
        ----------
        session: Session
            The database session.
        demo_id: int
            The ID of the demo to retrieve.

        Returns
        -------
        Demo
            The retrieved demo, or None if not found.
        """
        return _BaseDAO.get_by_id(session, Demo, demo_id)

    @staticmethod
    def get_all(session: Session,
                **kwargs
                ) -> Demo | None:
        """
        Retrieves a demo from the database.

        Parameters
        ----------
        session: Session
            The database session.

        Returns
        -------
        Demo
            The retrieved demo, or None if not found.
        """
        return _BaseDAO.get_all(session, Demo)

    @staticmethod
    def add(session: Session,
            demo: Demo
            ) -> None:
        """
        Adds a demo to the database.

        Parameters
        ----------
        session: Session
            The database session.
        demo: Demo
            The demo to add.
        """
        _BaseDAO.add(session, demo)
