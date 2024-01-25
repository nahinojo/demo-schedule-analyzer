from database import db
from models import Course, DemoEvent
from typing import List, Type


def create_course(
        course_code: str,
        instructor: str,
        term: str,
        year: int,
        demo_events: List[Type[DemoEvent]],
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
