"""
Fixtures for testing.
"""
import pytest
from flask import Flask
from datetime import datetime
from sqlalchemy.orm import Session
from app import create_app
from app.daos import CourseDAO
from app.models import Demo, DemoEvent, Course, Schedule
from app.database import Database
from app.services import ScheduleService


# App
@pytest.fixture()
def app(monkeypatch: pytest.MonkeyPatch) -> Flask:
    """
    Fixture to create Flask app based on the current environment.
    """
    monkeypatch.setenv("APP_ENV", "testing")
    app = create_app()
    yield app


# Database
@pytest.fixture
def db_session(app: Flask) -> Session:
    """
    Returns the database session.
    """
    with app.app_context():
        _session = Database.get_session()
        yield _session
        _session.close()


# Models
@pytest.fixture()
def demo() -> Demo:
    """
    Tests the creation of the demo model.
    """
    yield Demo(name="DEMO_TEST")


@pytest.fixture
def demo_event(demo) -> DemoEvent:
    """
    Tests the creation of the demo event model.
    """
    today = datetime.now().date()
    yield DemoEvent(
        event_date=today,
        additional_information="ADDITIONAL_INFORMATION_TEST",
        demos=[demo]
    )


@pytest.fixture
def course(demo_event) -> Course:
    """
    Tests the creation of the course model.
    """
    yield Course(
        course_code="COURSE_CODE_TEST",
        instructor="INSTRUCTOR_TEST",
        term="TERM_TEST",
        year=datetime.now().year,
        demo_events=[demo_event]
    )


@pytest.fixture
def schedule(course,
             db_session
             ) -> Schedule:
    """
    Tests the creation of the schedule model.
    """
    with db_session.begin():
        CourseDAO.add(session=db_session, course=course)
        db_session.flush()
        course_id = course.id
        schedule_service = ScheduleService(
            session=db_session,
            course_id=course_id
        )
        schedule_data = schedule_service.schedule_data
        print("schedule_data: ", schedule_data)
    yield Schedule(
        course_id=course_id,
        schedule_data=schedule_data
    )
