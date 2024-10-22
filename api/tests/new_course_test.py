"""
Tests the following:
    - Creation of the Course model.
    - Adding a Course to the database.
"""
from datetime import datetime
from flask import Flask
from sqlalchemy.orm import Session

from app.models import DemoEvent, Course
from app.daos import CourseDAO


def create_course_test(app: Flask,
                       db_session: Session,
                       course: Course,
                       demo_event: DemoEvent
                       ) -> None:
    """
    Tests the creation of the Course model, and associated child models.
    """
    assert course.course_code == "COURSE_CODE_TEST"
    assert course.instructor == "INSTRUCTOR_TEST"
    assert course.term == "TERM_TEST"
    assert course.year == datetime.now().year
    assert course.demo_events == [demo_event]


def add_course_to_db_test(db_session: Session,
                          course: Course
                          ) -> None:
    """
    Adds a course to the database.
    """
    with db_session.begin():
        course_dao = CourseDAO(db_session)
        prior_count = course_dao.get_count()
        course_dao.add(course)
        db_session.flush()
        post_count = course_dao.get_count()
        assert post_count == prior_count + 1
        db_session.rollback()
