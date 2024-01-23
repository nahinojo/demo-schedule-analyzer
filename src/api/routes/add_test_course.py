from models import Course, Demo, DemoEvent, db
from datetime import date


def add_test_course():
    print("Adding test course...")
    demo_1 = Demo(name="TEST_DEMO_1_NAME")
    demo_2 = Demo(name="TEST_DEMO_2_NAME")
    demo_event = DemoEvent(
        event_date=date(2005, 1, 1),
        additional_info="TEST_ADDITIONAL_INFO",
        demo=[demo_1, demo_2]
    )
    course = Course(
        course_code="TEST_COURSE_CODE",
        instructor="TEST_INSTRUCTOR",
        term="TEST_TERM",
        year=2005,
        demo_event=[demo_event]
    )
    db.session.add(course)
    db.session.commit()
    print("Test course added successfully!")
    result = {"status": "success", "message": "Test course added successfully"}, 204
    return result
