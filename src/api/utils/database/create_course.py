from database import db
from models import Course, DemoEvent
from typing import List


def create_course(
        course_code: str,
        instructor: str,
        term: str,
        year: int,
        demo_event: List[DemoEvent],
):
    course = Course(
        course_code=course_code,
        instructor=instructor,
        term=term,
        year=year,
        demo_event=demo_event
    )
    db.session.add(course)
    db.session.commit()
    return course
