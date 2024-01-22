from models import Course, DemoEvent, db


def add_course(
    course_code: str,
    instructor: str,
    term: str,
    year: int,
    demo_event: DemoEvent,
):
    course = Course(
        course_code=course_code,
        instructor=instructor,
        term=term,
        year=year,
        demo_event=[demo_event]
    )
    db.session.add(course)
    db.session.commit()
    return

