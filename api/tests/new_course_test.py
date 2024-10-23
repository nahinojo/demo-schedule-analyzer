"""
Tests the following:
    - Creation of the Course model.
    - Adding a Course to the database.
"""
from datetime import datetime
from flask import Flask
from sqlalchemy.orm import Session

from app.models import Course, DemoEvent, Demo
from app.daos import CourseDAO


def create_course_test(app: Flask,
                       db_session: Session,
                       course: Course,
                       demo_event: DemoEvent,
                       demo: Demo
                       ) -> None:
    """
    Tests the creation of the Course model and associated child models.

    Parameters
    ----------
    app: Flask
        The Flask app.
    db_session: Session
        The database session.
    course: Course
        The course fixture to be used for testing.
    demo_event: DemoEvent
        The demo_event fixture to be used for testing.
    demo: Demo
        The demo fixture to be used for testing.

    Returns
    -------
    None
    """
    assert course.course_code
    assert course.instructor
    assert course.term
    assert course.year
    assert course.demo_events[0] == demo_event
    assert demo_event.demos[0] == demo


def add_course_to_db_test(db_session: Session,
                          course: Course
                          ) -> None:
    """
    Tests adding a course to the database.

    Parameters
    ----------
    db_session: Session
        The database session.
    course: Course
        The course fixture to be used for testing.

    Returns
    -------
    None
    """
    with db_session.begin():
        course_dao = CourseDAO(db_session)
        prior_count = course_dao.count()
        course_dao.add(course)
        db_session.flush()
        post_count = course_dao.count()
        assert post_count == prior_count + 1
        db_session.rollback()
