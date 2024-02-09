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
                additional_info="TEST_ADDITIONAL_INFO",
                demos=[Demo(name="TEST_DEMO_NAME")]
            )
        ]
    )
    with Session() as session:
        print("verify no course:", session.get(Course, 1))
        stmt = select(Course).filter_by(id=1)
        items = session.scalars(stmt).first()
        if items:
            assert False
        session.add(new_course)
        session.commit()
        assert session.get(Course, 1).course_code == "TEST_COURSE_CODE"
        assert session.get(Course, 1).instructor == "TEST_INSTRUCTOR"
        assert session.get(Course, 1).term == "TEST_TERM"
        assert session.get(Course, 1).year == today.year
        assert session.get(Course, 1).demo_events[0].event_date == today
        assert session.get(Course, 1).demo_events[0].additional_info == "TEST_ADDITIONAL_INFO"
        assert session.get(Course, 1).demo_events[0].demos[0].name == "TEST_DEMO_NAME"
        yield
        """
        Solved the issue of session.get vs session.execute. This should be now be implementable through the repo.
        Unfortunately, time ran out. Complete later.
        """
        only_course = session.get(Course, 1)
        print("session.get(Course, 1):", only_course.serialize())
        stmt = select(Course).where(Course.id == 1)
        results = session.execute(stmt).scalars()
        for obj in results:
            print("session execute: ", obj.serialize())
        assert False
        session.delete(only_course)
        session.commit()
    # counter = 2
    # session.
    # while session.get(Course, counter):
    #     session.delete(session.get(Course, counter))
    #     session.get()
