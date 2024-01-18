from . import db


class Demo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
