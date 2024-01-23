from models import Course, DemoEvent, db
from typing import List


def add_course(
        course_code: str,
        instructor: str,
        term: str,
        year: int,
        demo_event: List[DemoEvent],
):
    print("Executing utils.database.add_course()...")
    course = Course(
        course_code=course_code,
        instructor=instructor,
        term=term,
        year=year,
        demo_event=[demo_event]
    )
    db.session.add(course)
    db.session.commit()
    print("Successfully added course:", course.serialize())
    return course.id
