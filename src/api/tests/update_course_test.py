from database import db
from models import Course, Demo, DemoEvent

import pytest
from datetime import date


@pytest.mark.usefixtures("app_context_with_test_course")
def update_course_test():
    retrieved_course = db.session.get(Course, 1)
    retrieved_course.course_code = "UPDATED_COURSE_CODE"
    retrieved_course.term = "UPDATED_TERM"
    retrieved_course.year = 2025
    retrieved_course.instructor = "UPDATED_INSTRUCTOR"
    updated_demos = [
        Demo(name="UPDATED_DEMO_1_NAME"),
        Demo(name="UPDATED_DEMO_2_NAME")
    ]
    updated_demo_event = DemoEvent(
        event_date=date(2006, 1, 1),
        additional_info="UPDATED_ADDITIONAL_INFO",
        demos=updated_demos
    )
    retrieved_course.demo_events = [updated_demo_event]
    db.session.commit()
    assert retrieved_course.course_code == "UPDATED_COURSE_CODE"
    assert retrieved_course.term == "UPDATED_TERM"
    assert retrieved_course.year == 2025
    assert retrieved_course.instructor == "UPDATED_INSTRUCTOR"
    assert retrieved_course.demo_events[0].event_date == date(2006, 1, 1)
    assert retrieved_course.demo_events[0].additional_info == "UPDATED_ADDITIONAL_INFO"
    assert retrieved_course.demo_events[0].demos[0].name == "UPDATED_DEMO_1_NAME"
    assert retrieved_course.demo_events[0].demos[1].name == "UPDATED_DEMO_2_NAME"
    return
