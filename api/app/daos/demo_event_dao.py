"""
DemoEvent DAO.
"""
from sqlalchemy.orm import Session
from app.models import DemoEvent
from ._base_dao import _BaseDAO


class DemoEventDAO(_BaseDAO):
    """
    DemoEvent DAO.
    """

    @staticmethod
    def get_by_id(session: Session,
                  demo_event_id: int,
                  **kwargs
                  ) -> DemoEvent | None:
        """
        Retrieves a demo event from the database.

        Parameters
        ----------
        session: Session
            The database session.
        demo_event_id: int
            The ID of the demo event to retrieve.

        Returns
        -------
        DemoEvent
            The retrieved demo event, or None if not found.
        """
        return _BaseDAO.get_by_id(session, DemoEvent, demo_event_id)

    @staticmethod
    def get_all(session: Session,
                **kwargs
                ) -> list[DemoEvent]:
        """
        Retrieves all demo events from the database.

        Parameters
        ----------
        session: Session
            The database session.

        Returns
        -------
        List[DemoEvent]
            The list of retrieved demo events.
        """
        return _BaseDAO.get_all(session, DemoEvent)

    @staticmethod
    def add(session: Session,
            demo_event: DemoEvent,
            **kwargs
            ) -> None:
        """
        Adds a demo event to the database.

        Parameters
        ----------
        session: Session
            The database session.
        demo_event: DemoEvent
            The demo event to add.
        """
        _BaseDAO.add(session, demo_event)
