"""
DemoEvent DAO.
"""

from app.database import Session
from app.models import DemoEvent

from sqlalchemy import select


class DemoEventDAO:
    """
    DemoEvent Data Access Object (DAO).
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

    def get(self, demo_event_id):
        """
        Retrieves a demo event from the database.

        Parameters
        ----------
        demo_event_id: int
            The ID of the demo event to retrieve.

        Returns
        -------
        DemoEvent
            The retrieved demo event, or None if not found.
        """
        return self.session.execute(
            select(DemoEvent).where(DemoEvent.id == demo_event_id)
        ).scalar_one_or_none()
