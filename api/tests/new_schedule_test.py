"""
Tests the following:
    - Creation of the schedule dictionary.
"""
from flask import Flask
from sqlalchemy.orm import Session

from app.models import Course
from app.daos.course_dao import CourseDAO
from app.services.schedule_service import ScheduleService


def create_schedule_test(app: Flask,
                         db_session: Session,
                         course: Course
                         ) -> None:
    """
    Tests the creation of the schedule dictionary.
    """
    with db_session.begin():
        course_dao = CourseDAO(session=db_session)
        course_dao.add(model=course)
        db_session.flush()
        schedule_service = ScheduleService(session=db_session,
                                           course_id=course.id)
        schedule_dict = schedule_service.schedule_dict
        assert schedule_dict
