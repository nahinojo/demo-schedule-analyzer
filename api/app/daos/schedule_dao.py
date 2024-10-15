"""
Schedule Data Access Object (DAO).
"""
from sqlalchemy.orm import Session
from app.models import Schedule
from ._base_dao import _BaseDAO


class ScheduleDAO(_BaseDAO):
    """
    Schedule Data Access Object (DAO).
    """

    @staticmethod
    def get_by_id(session: Session,
                  schedule_id: int,
                  **kwargs) -> Schedule | None:
        """
        Retrieves a schedule from the database.

        Parameters
        ----------
        session: Session
            The database session.
        schedule_id: int
            The ID of the schedule to retrieve.

        Returns
        -------
        Schedule
            The retrieved schedule, or None if not found.
        """
        return _BaseDAO.get_by_id(
            session=session,
            model=Schedule,
            model_id=schedule_id
        )

    @staticmethod
    def get_all(session: Session,
                **kwargs
                ) -> list[Schedule]:
        """
        Retrieves all schedules from the database.

        Parameters
        ----------
        session: Session
            The database session.

        Returns
        -------
        List[Schedule]
            The list of retrieved schedules.
        """
        return _BaseDAO.get_all(
            session=session,
            model=Schedule,
        )

    @staticmethod
    def add(session: Session,
            schedule: Schedule,
            ) -> None:
        """
        Adds a schedule to the database.

        Parameters
        ----------
        session: Session
            The database session.
        schedule: Schedule
            The schedule to add.
        """
        _BaseDAO.add(session, schedule)

    @staticmethod
    def get_count(session: Session,
                  **kwargs) -> int:
        """
        Counts the total number of schedules in the database.

        Parameters
        ----------
        session: Session
            The database session.

        Returns
        -------
        int
            The count of retrieved models.
        """
        return _BaseDAO.get_count(
            session=session,
            model=Schedule
        )
