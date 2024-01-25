from database import db
from models import Course

import pytest


@pytest.mark.usefixtures("app_context")
def delete_course_test(test_course):
    db.session.add(test_course)
    db.session.commit()
    retrieved_course = db.session.get(Course, 1)
    db.session.delete(retrieved_course)
    db.session.commit()
    assert db.session.get(Course, 1) is None
    return
