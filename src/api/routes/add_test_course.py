from models import Course, Demo, DemoEvent, db


def add_test_course():
    demo_1 = Demo(name="TEST_DEMO_1_NAME")
    demo_2 = Demo(name="TEST_DEMO_2_NAME")
    demo_event = DemoEvent(
        date="2023-01-01",
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
