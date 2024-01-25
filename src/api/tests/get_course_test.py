from database import db
from models import Course

import pytest


@pytest.mark.usefixtures("app_context_with_test_course")
def get_course_test(test_course):
    retrieved_course = db.session.get(Course, 1)
    assert retrieved_course == test_course
