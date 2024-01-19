from flask import jsonify
from models import Course


def get_courses():
    print("Extracting courses...")
    courses = Course.query.all()
    courses = jsonify([course.serialize() for course in courses])
    if not courses:
        return jsonify({"message": "No courses found"}), 404
    else:
        return courses
