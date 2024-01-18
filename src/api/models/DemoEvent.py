from . import db


class DemoEvent (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    demos = db.relationship("Demo", backref="demo_event", lazy=True)
    additional_info = db.Column(db.Text)

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "demos": [demo.serialize() for demo in self.demos],
            "additional_info": self.additional_info
        }
