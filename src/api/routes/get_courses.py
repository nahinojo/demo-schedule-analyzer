from models import Course, db
from flask import jsonify
from sqlalchemy import select


def get_courses():
    print("Getting courses...")
    result = db.session.execute(db.select(Course))
    courses = result.fetchall()
    print("courses:", courses)
    if not courses:
        return jsonify({"message": "No courses found"}), 404
    return jsonify([courses[0].serialize() for courses in courses]), 200
