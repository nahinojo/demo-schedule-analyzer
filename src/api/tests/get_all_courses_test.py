from database import db
from models import Course
from flask import jsonify


def get_all_courses_test(client):
    # courses = db.session.execute(db.select(Course)).scalars().all()
    # return jsonify([c.serialize() for c in courses])
    print("Executing utils.database.get_all_courses()...")
    return
