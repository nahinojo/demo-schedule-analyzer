from database import db
from models import Course, Demo, DemoEvent
from datetime import date


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
    result = {"status": "success", "message": "Test course added successfully"}, 204
    return result
