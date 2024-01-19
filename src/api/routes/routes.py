from flask import Blueprint
from . import get_courses, add_course, add_test_course

api = Blueprint('api', __name__)

api.route('/get_courses', methods=['GET'])(get_courses)
api.route('/add_course', methods=['POST'])(add_course)
api.route('/add_test_course', methods=['POST'])(add_test_course)

