"""
Handles schedule data operations.
"""
from sqlalchemy.orm import Session

from app.database import Database
from app.daos import CourseDAO


class ScheduleService:
    """
    Handles schedule data operations.

    Primary use case:
    - Construct schedule data from course.
    - Add schedule to database.
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
        """
        return self._schedule_dict

    def _create_schedule(self) -> dict:
        """
        Constructs the schedule dictionary from the course.
        """
        with Database.get_session() as session:
            course = CourseDAO.get_by_id(session, self.course_id)
            session.expunge_all()
        schedule = {"course_code": course.course_code,
                    "instructor": course.instructor,
                    "term": course.term, "year": course.year,
                    "events": [],
                    }
        for demo_event in course.demo_events:
            schedule["events"].append(
                {
                    "date": demo_event.event_date,
                    "demos": [demo.name for demo in demo_event.demos],
                    "additional_info": demo_event.additional_information
                }
            )
        return schedule
