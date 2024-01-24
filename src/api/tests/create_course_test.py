from database import db
from models import Course, Demo, DemoEvent

import pytest
from datetime import date


@pytest.mark.usefixtures("app_context")
def create_course_test():
    demo_1 = Demo(name="DEMO_1_NAME_TEST")
    demo_2 = Demo(name="DEMO_2_NAME_TEST")
    demo_event = DemoEvent(
        event_date=date(2005, 1, 1),
        additional_info="ADDITIONAL_INFO_TEST",
        demo=[demo_1, demo_2]
    )
    course = Course(
        course_code="COURSE_CODE_TEST",
        instructor="INSTRUCTOR_TEST",
        term="TERM_TEST",
        year=2024,
        demo_event=[demo_event]
    )
    db.session.add(course)
    db.session.commit()
    test_course = db.session.get(Course, 1)
    test_course = test_course.serialize()
    assert test_course == {
        'id': 1,
        'course_code': 'COURSE_CODE_TEST',
        'instructor': 'INSTRUCTOR_TEST',
        'term': 'TERM_TEST', 'year': 2024,
        'demo_event': [
            {'id': 1,
             'date': date(2005, 1, 1),
             'demos': [{'id': 1, 'name': 'DEMO_1_NAME_TEST'},
                       {'id': 2, 'name': 'DEMO_2_NAME_TEST'}],
             'additional_info': 'ADDITIONAL_INFO_TEST'}
        ]
    }

