from database import db
from models import Demo


class DemoEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_date = db.Column(db.Date)
    additional_info = db.Column(db.Text)
    demo = db.relationship("Demo", backref="demo_event")
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))

    def add_demo(
            self,
            name: str,
    ):
        demo = Demo(
            name=name,
            demo_event_id=self.demo_event_id
        )
        db.session.add(demo)
        db.session.commit()
        return demo

    def serialize(self):
        return {
            "id": self.id,
            "date": self.event_date,
            "demos": [demo.serialize() for demo in self.demo],
            "additional_info": self.additional_info
        }
