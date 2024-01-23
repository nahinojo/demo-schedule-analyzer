from flask import Blueprint
from . import get_all_courses, add_test_course

test = Blueprint('api', __name__)
test.route('/get_all_courses', methods=['GET'])(get_all_courses)
test.route('/add_test_course', methods=['POST'])(add_test_course)



