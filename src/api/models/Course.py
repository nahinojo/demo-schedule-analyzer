from . import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(10), unique=True, nullable=False)
    instructor = db.Column(db.String(80), nullable=False)
    term = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    demo_events = db.relationship("DemoEvent", backref="course", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "course_code": self.course_code,
            "instructor": self.instructor,
            "term": self.term,
            "year": self.year,
            "demo_events": [demo_event.serialize() for demo_event in self.demo_events]
        }


x = Course.query.all()
