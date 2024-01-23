from database import db
from models import Course
from flask import jsonify


def get_all_courses():
    print("Getting courses...")
    courses = db.session.execute(db.select(Course)).scalars().all()
    print("courses:", courses)
    return jsonify([c.serialize() for c in courses])
