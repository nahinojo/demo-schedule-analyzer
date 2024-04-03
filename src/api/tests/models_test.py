import pytest


@pytest.mark.usefixtures("app_context_with_test_data")
def crud_course_test():
    """
    Tests CRUD operations for Course model.

    Only executes Update operation because Create, Read, and Delete are inherently performed in the setup and teardown
    of the fixture app_context_with_data.
    """
    from app.database import Session
    from app.models import Course
    with Session() as session:
        course = session.get(Course, 1)
        course.course_code = "TEST_COURSE_CODE_UPDATE"
        course.instructor = "TEST_INSTRUCTOR_UPDATE"
        course.term = "TEST_TERM_UPDATE"
        course.year = 2020
        session.commit()
        assert session.get(Course, 1)
        db_course = session.get(Course, 1)
        assert db_course.course_code == "TEST_COURSE_CODE_UPDATE"
        assert db_course.instructor == "TEST_INSTRUCTOR_UPDATE"
        assert db_course.term == "TEST_TERM_UPDATE"
        assert db_course.year == 2020


@pytest.mark.usefixtures("app_context_with_test_data")
def crud_demo_event_test():
    """
    Tests CRUD operations for DemoEvent model.
    """
    import datetime

    from app.database import Session
    from app.models import Course, Demo, DemoEvent
    from sqlalchemy import select
    new_demo = Demo(name="DEMO_NAME_CRUD_DEMO_EVENT")
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    new_demo_event = DemoEvent(
        event_date=yesterday,
        additional_information="ADDITIONAL_INFO_CRUD_DEMO_EVENT",
        demos=[new_demo]
    )
    with Session() as session:
        session.add(new_demo_event)
        course = session.get(Course, 1)
        course.demo_events.append(new_demo_event)
        session.add(course)
        session.commit()
        assert session.get(DemoEvent, 2)
        db_new_demo_event = session.get(DemoEvent, 2)
        assert db_new_demo_event.event_date == yesterday
        assert db_new_demo_event.additional_information == "ADDITIONAL_INFO_CRUD_DEMO_EVENT"
        assert db_new_demo_event.demos[0].name == "DEMO_NAME_CRUD_DEMO_EVENT"
        session.delete(new_demo_event)
        session.delete(new_demo)
        session.commit()
        stmt = select(Demo)
        items = session.scalars(stmt).all()
        serialized_items = [item.serialize() for item in items]
        assert session.get(DemoEvent, 2) is None


@pytest.mark.usefixtures("app_context_with_test_data")
def crud_demo_test():
    """
    Tests CRUD operations for Demo model.
    """
    from app.database import Session
    from app.models import Course, Demo
    from sqlalchemy import select
    new_demo = Demo(name="DEMO_NAME_CRUD_DEMO")
    with Session() as session:
        stmt = select(Demo)
        items = session.scalars(stmt).all()
        serialized_items = [item.serialize() for item in items]
        stmt = select(Course)
        items = session.scalars(stmt).all()
        serialized_items = [item.serialize() for item in items]
        session.add(new_demo)
        course = session.get(Course, 1)
        course.demo_events[0].demos.append(new_demo)
        session.commit()
        assert session.get(Demo, 1)
        db_new_demo = session.get(Demo, 2)
        assert db_new_demo.name == "DEMO_NAME_CRUD_DEMO"
        session.delete(new_demo)
        session.commit()
        assert session.get(Demo, 2) is None
