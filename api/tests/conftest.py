"""
Fixtures for testing.
"""
import pytest
from _pytest.monkeypatch import MonkeyPatch


@pytest.fixture()
def app(monkeypatch: MonkeyPatch):
    """
    Fixture for the Flask app.
    """
    monkeypatch.setenv("APP_ENV", "testing")
    from app import create_app
    app = create_app()
    yield app


@pytest.fixture()
def app_context(app):
    """
    Fixture for the Flask app context.
    """
    with app.app_context():
        print("Starting app context")
        yield
        print("Ending app context")


@pytest.fixture()
def app_context_with_test_data(app_context):
    """
    Setups the database with test data.
    """
    print("initializing app context with test data")
    from datetime import date
    from app.models import Course, Demo, DemoEvent
    from app.database.utils import session_scope
    from app.daos import CourseDAO
    with session_scope() as session:
        try:
            course_code = CourseDAO.get_by_id(session, 1).course_code
        except Exception:
            course_code = None
        if course_code is not None:
            print("course code: ", course_code)
        assert CourseDAO.get_by_id(session, 1) is None
    today = date.today()
    course = Course(
        course_code="TEST_COURSE_CODE",
        instructor="TEST_INSTRUCTOR",
        term="TEST_TERM",
        year=today.year,
        demo_events=[
            DemoEvent(
                event_date=today,
                additional_information="TEST_ADDITIONAL_INFO",
                demos=[
                    Demo(name="TEST_DEMO_NAME")
                ]
            )
        ]
    )
    with session_scope() as session:
        CourseDAO.add(session, course)
        course = CourseDAO.get_by_id(session, 1)
        assert course
        assert course.course_code == "TEST_COURSE_CODE"
        assert course.instructor == "TEST_INSTRUCTOR"
        assert course.term == "TEST_TERM"
        assert course.year == today.year
        assert course.demo_events[0].event_date == today
        assert (
                course.demo_events[0].additional_information
                == "TEST_ADDITIONAL_INFO"
        )
    yield
    with session_scope() as session:
        session.delete(course)
        session.commit()


@pytest.fixture()
def app_context_with_real_data(app_context, cleanup):
    """
    Setups the database with data from the demo calendar.
    """
    print("initializing app context with real data")
    from app.database.utils import update_db_from_calendar
    update_db_from_calendar(app_context)
    yield
    cleanup()


@pytest.fixture()
def cleanup(app):
    """
    Clears the database after each test.
    """
    print("initializing cleanup")
    yield
    print("running cleanup")
    import os
    paths = [
        app.config["DATABASE_PATH"],
        app.config["CALENDAR_PATH"],
        app.config["SCHEDULE_XLSX_PATH"]
    ]
    for path in paths:
        if os.path.isfile(path):
            os.remove(path)
    del app
