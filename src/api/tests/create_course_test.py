import pytest
from app.database import Session
from app.models import Course, DemoEvent, Demo
from datetime import date


@pytest.mark.usefixtures("app_context")
def create_object_test():
    with Session() as session:
        new_course = Course(
            course_code="TEST_COURSE_CODE",
            instructor="TEST_INSTRUCTOR",
            term="TEST_TERM",
            year=2000,
            demo_events=[
                DemoEvent(
                    event_date=date.today(),
                    additional_info="TEST_ADDITIONAL_INFO",
                    demos=[Demo(name="TEST_DEMO_NAME")]
                )
            ]
        )
        session.add(new_course)
        session.commit()
        assert session.get(Course, 1).course_code == "TEST_COURSE_CODE"
        assert session.get(Course, 1).instructor == "TEST_INSTRUCTOR"
        assert session.get(Course, 1).term == "TEST_TERM"
        assert session.get(Course, 1).year == 2000
        assert session.get(Course, 1).demo_events[0].event_date == date.today()
        assert session.get(Course, 1).demo_events[0].additional_info == "TEST_ADDITIONAL_INFO"
        assert session.get(Course, 1).demo_events[0].demos[0].name == "TEST_DEMO_NAME"
