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
        yield


@pytest.fixture()
def app_context_with_test_data(app_context):
    """
    Setups the database with test data.
    """
    from datetime import date
    from app.models import Course, Demo, DemoEvent
    from app.daos import CourseDAO
    today = date.today()
    new_course = Course(
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
    CourseDAO.`
    # with Session() as session:
    #     # stmt = select(Course).filter_by(id=1)
    #     # TODO: Check if stmt has an item.
    #     session.add(new_course)
    #     session.commit()
    #     only_course = session.get(Course, 1)
    #     assert only_course
    #     assert only_course.course_code == "TEST_COURSE_CODE"
    #     assert only_course.instructor == "TEST_INSTRUCTOR"
    #     assert only_course.term == "TEST_TERM"
    #     assert only_course.year == today.year
    #     assert only_course.demo_events[0].event_date == today
    #     assert (
    #             only_course.demo_events[0].additional_information
    #             == "TEST_ADDITIONAL_INFO"
    #     )
    #     assert only_course.demo_events[0].demos[0].name == "TEST_DEMO_NAME"
    #     del only_course
    #     yield
    #     only_course = session.get(Course, 1)
    #     session.delete(only_course)
    #     session.commit()
    #     assert session.get(Course, 1) is None


@pytest.fixture()
def app_context_with_real_data(app_context):
    """
    Setups the database with data from the demo calendar.
    """
    from app.database.fill_db_from_calendar import fill_db_from_calendar
    from app.database.clear_db import clear_db
    fill_db_from_calendar()
    yield
    clear_db()
    return
