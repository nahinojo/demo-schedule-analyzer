"""
Testing for Course model.
"""
from datetime import datetime
from flask import Flask
from sqlalchemy.orm import Session

from app.models import DemoEvent, Course
from app.daos import CourseDAO


def course_test(app: Flask,
                course: Course,
                demo_event: DemoEvent
                ) -> None:
    """
    Tests the creation of the course model.
    """
    with app.app_context():
        assert course.course_code == "COURSE_CODE_TEST"
        assert course.instructor == "INSTRUCTOR_TEST"
        assert course.term == "TERM_TEST"
        assert course.year == datetime.now().year
        assert course.demo_events == [demo_event]


def add_course_to_db_test(db_session: Session,
                          course: Course
                          ) -> None:
    """
    Tests the adding of a course to the database.
    """
    with db_session.begin():
        count = CourseDAO.get_count(db_session)
        CourseDAO.add(db_session, course)
        assert count == CourseDAO.get_count(db_session) - 1
