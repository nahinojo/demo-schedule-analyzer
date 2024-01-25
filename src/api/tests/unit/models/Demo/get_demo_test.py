from database import db
from models import DemoEvent

import pytest


@pytest.mark.usefixtures("app_context_with_test_course")
def get_demo_test(test_demo_event):
    retrieved_demo_event = db.session.get(DemoEvent, 1)
    assert retrieved_demo_event == test_demo_event
