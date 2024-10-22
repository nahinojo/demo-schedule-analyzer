"""
Tests the following:
    - Creation of the schedule dictionary.
"""
from flask import Flask
from sqlalchemy.orm import Session

from app.database import Database
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
        CourseDAO.add(db_session, course)