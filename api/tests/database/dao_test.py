"""
Test the DAOs.
"""

import pytest


@pytest.mark.usefixtures("app_context_with_test_data")
def course_dao_test():
    """
    Course retrieval.
    """
    from app.database import Database
    from app.daos import CourseDAO

    with Database.Session() as session:
        course_dao = CourseDAO(session=session)
        course = course_dao.get(course_id=1)
        assert course.course_code == "TEST_COURSE_CODE"


@pytest.mark.usefixtures("app_context_with_test_data")
def demo_event_dao_test():
    """
    DemoEvent retrieval.
    """
    from app.database import Database
    from app.daos import DemoEventDAO

    with Database.Session() as session:
        demo_event_dao = DemoEventDAO(session=session)
        demo_event = demo_event_dao.get(1)
        assert demo_event.additional_information == "TEST_ADDITIONAL_INFO"


@pytest.mark.usefixtures("app_context_with_test_data")
def demo_dao_test():
    """
    Demo retrieval,
    """
    from app.database import Database
    from app.daos import DemoDAO

    with Database.Session() as session:
        demo_dao = DemoDAO(session=session)
        demo = demo_dao.get(1)
        assert demo.name == "TEST_DEMO_NAME"
