from flask import jsonify
from models import Course


def get_courses():
    courses = Course.query.all()
    return jsonify([course.serialize() for course in courses])
