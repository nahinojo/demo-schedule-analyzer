"""
Handles schedule data operations.
"""
import json
from sqlalchemy.orm import Session
from sqlalchemy import JSON

from app.models import Schedule
from app.database import Database
from app.daos import CourseDAO, ScheduleDAO


class ScheduleService:
    """
    Handles schedule data operations.
    """

    def __init__(self,
                 session: Session,
                 course_id: int
                 ) -> None:
        self._session = session
        self._schedule_data = self._get_schedule_data(course_id=course_id)

    @property
    def schedule_data(self) -> JSON:
        """
        Returns the schedule_data.
        """
        return self._schedule_data

    def _get_schedule_data(self, course_id: int) -> JSON:
        """
        Retrieves the schedule data from the database. Creates it if it does
        not exist.
        """
        with Database.get_session() as session:
            course = CourseDAO.get_by_id(session, 1)
            if course.schedule:
                schedule: Schedule = course.schedule
                schedule_data = schedule.schedule_data
            else:
                schedule_data = self._create_schedule_data(
                    course_id=course_id,
                    session=session
                )
                schedule = Schedule(
                    course_id=course_id,
                    schedule_data=schedule_data
                )
                ScheduleDAO.add(session, schedule)
                Database.commit_session()
            return schedule_data

    @staticmethod
    def _create_schedule_data(course_id: int,
                              session: Session
                              ) -> JSON:
        """
        Creates the schedule data from scratch.
        """
        schedule_data_dict = {
            "course_code": None,
            "instructor": None,
            "term": None,
            "year": None,
            "events": []
        }
        course = CourseDAO.get_by_id(session, course_id)
        schedule_data_dict["course_code"] = course.course_code
        schedule_data_dict["instructor"] = course.instructor
        schedule_data_dict["term"] = course.term
        schedule_data_dict["year"] = course.year
        demo_events = course.demo_events
        for demo_event in demo_events:
            schedule_data_dict["events"].append(
                {
                    # Change date to week number or some other string-based
                    # format. Cannot add schedule to db as JSON otherwise.
                    "date": demo_event.event_date.isoformat(),
                    "demos": [demo.name for demo in demo_event.demos],
                    "additional_info": demo_event.additional_information
                }
            )
        print("schedule_data_dict: ", schedule_data_dict)
        schedule_data = json.dumps(schedule_data_dict)
        return schedule_data_dict
