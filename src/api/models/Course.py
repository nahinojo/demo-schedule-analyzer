from database import db
from models import DemoEvent
from typings import Demos

from datetime import date


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(10))
    instructor = db.Column(db.String(80))
    term = db.Column(db.String(80))
    year = db.Column(db.Integer)
    demo_events = db.relationship("DemoEvent", backref="course")

    def add_demo_event(
            self,
            event_date: date,
            additional_info: str,
            demos: Demos
    ):
        demo_event = DemoEvent(
            event_date=event_date,
            additional_info=additional_info,
            demo=demos,
            course_id=self.id
        )
        db.session.add(demo_event)
        db.session.commit()
        return demo_event

    def serialize(self):
        return {
            "id": self.id,
            "course_code": self.course_code,
            "instructor": self.instructor,
            "term": self.term,
            "year": self.year,
            "demo_events": [demo_event.serialize() for demo_event in self.demo_events]
        }
