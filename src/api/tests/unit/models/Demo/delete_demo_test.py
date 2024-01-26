from database import db
from models import Course, Demo

import pytest


@pytest.mark.usefixtures("app_context")
def delete_demo_test(test_course):
    test_demo = Demo(name="DELETE_DEMO_TEST")
    test_course.demo_events.demos = [test_demo]
    db.session.add(test_demo)
    db.session.commit()
    db.session.delete(test_demo)
    db.session.commit()
    assert db.session.get(Demo, 1) is None
    return
