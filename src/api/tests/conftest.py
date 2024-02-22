import pytest


@pytest.fixture()
def app():
    from app import app
    app.config.from_object('app.config.TestingConfig')
    yield app
    return


@pytest.fixture()
def app_context(app):
    with app.app_context():
        yield
    return


@pytest.fixture()
def app_context_with_data(app_context):
    from app.database import Session
    from app.models import Course, DemoEvent, Demo
    from datetime import date
    from sqlalchemy import select
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
    with Session() as session:
        stmt = select(Course).filter_by(id=1)
        items = session.scalars(stmt).first()
        if items:
            assert False
        session.add(new_course)
        session.commit()
        only_course = session.get(Course, 1)
        assert only_course
        assert only_course.course_code == "TEST_COURSE_CODE"
        assert only_course.instructor == "TEST_INSTRUCTOR"
        assert only_course.term == "TEST_TERM"
        assert only_course.year == today.year
        assert only_course.demo_events[0].event_date == today
        assert only_course.demo_events[0].additional_information == "TEST_ADDITIONAL_INFO"
        assert only_course.demo_events[0].demos[0].name == "TEST_DEMO_NAME"
        del only_course
        yield
        only_course = session.get(Course, 1)
        session.delete(only_course)
        session.commit()
        assert session.get(Course, 1) is None
