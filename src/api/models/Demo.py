from database import db


class Demo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    demo_event_id = db.Column(db.Integer, db.ForeignKey("demo_event.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
