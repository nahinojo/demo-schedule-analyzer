from database import db
from models import Course, Demo, DemoEvent

import pytest
from datetime import date


@pytest.mark.usefixtures("app_context_with_test_course")
def update_course_test():
    retrieved_course = db.session.get(Course, 1)
    retrieved_course.course_code = "UPDATE_COURSE_CODE_TEST"
    retrieved_course.term = "UPDATE_TERM_TEST"
    retrieved_course.year = 2025
    retrieved_course.instructor = "UPDATE_INSTRUCTOR_TEST"
    updated_demos = [
        Demo(name="UPDATE_DEMO_1_NAME_TEST"),
        Demo(name="UPDATE_DEMO_2_NAME_TEST")
    ]
    updated_demo_event = DemoEvent(
        event_date=date(2006, 1, 1),
        additional_info="UPDATE_ADDITIONAL_INFO_TEST",
        demos=updated_demos
    )
    retrieved_course.demo_events = [updated_demo_event]
    db.session.commit()
    assert retrieved_course.course_code == "UPDATE_COURSE_CODE_TEST"
    assert retrieved_course.term == "UPDATE_TERM_TEST"
    assert retrieved_course.year == 2025
    assert retrieved_course.instructor == "UPDATE_INSTRUCTOR_TEST"
    assert retrieved_course.demo_events[0].event_date == date(2006, 1, 1)
    assert retrieved_course.demo_events[0].additional_info == "UPDATE_ADDITIONAL_INFO_TEST"
    assert retrieved_course.demo_events[0].demos[0].name == "UPDATE_DEMO_1_NAME_TEST"
    assert retrieved_course.demo_events[0].demos[1].name == "UPDATE_DEMO_2_NAME_TEST"
    return
