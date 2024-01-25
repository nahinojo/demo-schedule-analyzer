from database import db
from models import Course
from typings import DemoEvents


def create_course(
        course_code: str,
        instructor: str,
        term: str,
        year: int,
        demo_events: DemoEvents,
):
    course = Course(
        course_code=course_code,
        instructor=instructor,
        term=term,
        year=year,
        demo_event=demo_events
    )
    db.session.add(course)
    db.session.commit()
    return course
