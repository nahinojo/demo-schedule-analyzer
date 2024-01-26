from database import db
from models import Course

import pytest
from datetime import date


@pytest.mark.usefixtures("app_context_with_test_course")
def update_demo_test():
    retrieved_course = db.session.get(Course, 1)
    retrieved_demo_event = retrieved_course.demo_events[0]
    retrieved_demo_event.event_date = date(2006, 1, 1)
    retrieved_demo_event.additional_info = "UPDATE_ADDITIONAL_INFO_TEST"
    retrieved_demo_event.demos[0].name = "UPDATE_DEMO_NAME_TEST"
    db.session.commit()
    assert retrieved_course.demo_events[0].event_date == date(2006, 1, 1)
    assert retrieved_course.demo_events[0].additional_info == "UPDATE_ADDITIONAL_INFO_TEST"
    assert retrieved_course.demo_events[0].demos[0].name == "UPDATE_DEMO_NAME_TEST"
    return
