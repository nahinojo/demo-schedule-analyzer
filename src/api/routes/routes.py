from flask import Blueprint
from . import get_all_courses, add_test_course

api = Blueprint('api', __name__)

api.route('/get_all_courses', methods=['GET'])(get_all_courses)
api.route('/add_test_course', methods=['POST'])(add_test_course)

