from database import db
from models import Course, Demo

import pytest


@pytest.mark.usefixtures("app_context_with_test_course")
def create_demo_test():
    test_demo = Demo(name="CREATE_DEMO_NAME_TEST")
    test_course = db.session.get(Course, 1)
    test_course.demo_events[0].demos = [test_demo]
    db.session.commit()
    assert test_course.demo_events[0].demos[0].name == "CREATE_DEMO_NAME_TEST"
    return
