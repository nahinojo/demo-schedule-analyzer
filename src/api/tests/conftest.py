from create_app import create_app
from models import Course, Demo, DemoEvent
from database import db

import pytest
from datetime import date


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app
    return


@pytest.fixture()
def app_context(app):
    with app.app_context():
        yield
    return


@pytest.fixture()
def test_course():
    demo_1 = Demo(name="DEMO_1_NAME")
    demo_2 = Demo(name="DEMO_2_NAME")
    demo_event = DemoEvent(
        event_date=date(2005, 1, 1),
        additional_info="ADDITIONAL_INFO",
        demos=[demo_1, demo_2]
    )
    return Course(
        course_code="COURSE_CODE",
        instructor="INSTRUCTOR",
        term="TERM",
        year=2024,
        demo_events=[demo_event]
    )


@pytest.fixture()
def app_context_with_test_course(app_context, test_course):
    db.session.add(test_course)
    db.session.commit()
    yield
    db.session.delete(test_course)
    return
