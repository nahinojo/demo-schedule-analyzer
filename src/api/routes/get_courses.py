from flask import jsonify
from ..models import Course

x = Course.query.all()


def get_courses():
    courses = Course.query.all()
    return jsonify([course.serialize() for course in courses])
