"""
Fixtures for testing.
"""
import pytest
from flask import Flask
from datetime import datetime
from sqlalchemy.orm import Session

from app import create_app
from app.models import Demo, DemoEvent, Course
from app.database import Database


# App
@pytest.fixture()
def app(monkeypatch: pytest.MonkeyPatch) -> Flask:
    """
    Flask app fixture for testing.
    """
    monkeypatch.setenv("APP_ENV", "testing")
    app = create_app()
    yield app


# Database
@pytest.fixture
def db_session(app: Flask) -> Session:
    """
    Database session.
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
