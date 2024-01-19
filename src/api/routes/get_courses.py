from flask import jsonify, request
from models import Course


def get_courses():
    request.args.get()
    courses = Course.query.all()
    if not courses:
        return jsonify({"message": "No courses found"}), 404
    courses = jsonify([course.serialize() for course in courses])
    return courses
