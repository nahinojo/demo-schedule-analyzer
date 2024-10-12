"""
Demo DAO.
"""
from app.database import Session
from app.models import Demo

from sqlalchemy import select


class DemoDAO:
    """
    Demo Data Access Object (DAO).
    """

    def __init__(self, session: Session):
        """
        Initializes the DAO.

        Parameters
        ----------
        session: Session
            The session to use for database operations.
        """
        self.session = session

    def get(self, demo_id) -> Demo:
        """
        Retrieves a demo from the database.

        Parameters
        ----------
        demo_id: int
            The ID of the demo to retrieve.

        Returns
        -------
        Demo
            The retrieved demo, or None if not found.
        """
        return self.session.execute(
            select(Demo).where(Demo.id == demo_id)
        ).scalar_one_or_none()
