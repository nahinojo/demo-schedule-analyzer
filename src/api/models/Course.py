from . import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(10), nullable=False)
    instructor = db.Column(db.String(80), nullable=False)
    term = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    demo_event = db.relationship("DemoEvent", backref="course", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "course_code": self.course_code,
            "instructor": self.instructor,
            "term": self.term,
            "year": self.year,
            "demo_event": [demo_event.serialize() for demo_event in self.demo_event]
        }

