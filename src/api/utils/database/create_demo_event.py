from database import db
from models import Course, Demo, DemoEvent

from datetime import date
from typing import List


def create_demo_event(
        event_date: date,
        additional_info: str,
        demo: List[Demo],
        course_id: int
):
    print("Executing utils.database.create_demo_event()...")
    course = db.session.get(Course, course_id)
    if course:
        demo_event = DemoEvent(
            event_date=event_date,
            additional_info=additional_info,
            demo=demo,
            course_id=course_id
        )
        db.session.add(demo_event)
        db.session.commit()
        print("Successfully added demo event:", demo_event.serialize())
    else:
        print("Course not found.")
    return demo_event.id
