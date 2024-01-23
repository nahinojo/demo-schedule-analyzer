from flask import Blueprint
from . import get_all_courses, add_test_course, add_and_edit_course

test_blueprint = Blueprint('test', __name__)
test_blueprint.route('/add_and_edit_course', methods=['POST'])(add_and_edit_course)
test_blueprint.route('/add_test_course', methods=['POST'])(add_test_course)
test_blueprint.route('/get_all_courses', methods=['GET'])(get_all_courses)
