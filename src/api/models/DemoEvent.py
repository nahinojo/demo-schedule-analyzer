from . import db


class DemoEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_date = db.Column(db.Date, nullable=False)
    demo = db.relationship("Demo", backref="demo_event", lazy=True)
    additional_info = db.Column(db.Text)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "date": self.event_date,
            "demos": [demo.serialize() for demo in self.demo],
            "additional_info": self.additional_info
        }
