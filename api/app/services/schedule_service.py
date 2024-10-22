"""
Handles schedule data operations.
"""
from sqlalchemy.orm import Session

from app.database import Database
from app.daos import CourseDAO


class ScheduleService:
    """
    Handles schedule data operations.
    """
    def __init__(self,
                 session: Session,
                 course_id: int
                 ):
        """
        Initializes the ScheduleService class.

        Parameters
        ----------
        session: Session
            The database session.
        course_id: int
            The ID of the course to construct the schedule for.
        """
        self._session = session
        self._course_id = course_id
        self._schedule_dict = self._create_schedule()

    @property
    def course_id(self) -> int:
        """
        Returns the course ID.
        """
        return self._course_id

    @property
    def schedule_dict(self) -> dict:
        """
        Returns the schedule dictionary.

        Returns
        -------
        dict
            The schedule dictionary.
        """
        return self._schedule_dict

    def _create_schedule(self) -> dict:
        """
        Constructs a new schedule.

        Returns
        -------
        schedule_dict: dict
            The constructed schedule dictionary.
        """
        with Database.get_session() as session:
            course = CourseDAO.get_by_id(session, self.course_id)
            session.expunge_all()
        schedule_dict = {"course_code": course.course_code,
                         "instructor": course.instructor,
                         "term": course.term, "year": course.year,
                         "events": [],
                         }
        for demo_event in course.demo_events:
            schedule_dict["events"].append(
                {
                    "date": demo_event.event_date,
                    "demos": [demo.name for demo in demo_event.demos],
                    "additional_info": demo_event.additional_information
                }
            )
        return schedule_dict
