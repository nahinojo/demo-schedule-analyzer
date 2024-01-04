import os
from utils.generate_schedule import generate_schedule, SCHEDULE_FILE_NAME
from utils.get_course_attribute_options import get_course_attribute_options
from utils.extract_course_details_from_calendar import extract_course_details_from_calendar
from flask import Flask, request, send_file, render_template

app = Flask(__name__)


@app.route('/create_schedule', methods=['GET'])
def create_schedule():
    target_course_code = request.args.get('target_course_code', None)
    target_instructor = request.args.get('target_instructor', None)
    target_term = request.args.get('target_term', None)
    target_year = request.args.get('target_year', None)
    target_year = int(target_year)
    is_target_year_as_minimum = request.args.get('is_target_year_as_minimum', True)
    if type(is_target_year_as_minimum) == str:
        if is_target_year_as_minimum.lower() == "true":
            is_target_year_as_minimum = True
        elif is_target_year_as_minimum.lower() == "false":
            is_target_year_as_minimum = False
    generate_schedule(
        target_course_code=target_course_code,
        target_instructor=target_instructor,
        target_term=target_term,
        target_year=target_year,
        is_target_year_as_minium=is_target_year_as_minimum
    )
    parent_path = os.getcwd() + '/src'
    return send_file(f"{parent_path}/build/{SCHEDULE_FILE_NAME}", as_attachment=True)


@app.route('/course_attribute_options', methods=['GET'])
def course_attribute_options():
    target_course_code = request.args.get('target_course_code', None)
    target_instructor = request.args.get('target_instructor', None)
    target_term = request.args.get('target_term', None)
    target_year = request.args.get('target_year', None)
    target_year = int(target_year)
    is_target_year_as_minimum = request.args.get('is_target_year_as_minimum', True)
    if type(is_target_year_as_minimum) == str:
        if is_target_year_as_minimum.lower() == "true":
            is_target_year_as_minimum = True
        elif is_target_year_as_minimum.lower() == "false":
            is_target_year_as_minimum = False
    course_details = extract_course_details_from_calendar(
        target_course_code=target_course_code,
        target_instructor=target_instructor,
        target_term=target_term,
        target_year=target_year,
        is_target_year_as_minium=is_target_year_as_minimum
    )
    print("course_details:", course_details)
    return get_course_attribute_options(course_details)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/test')
def test():
    return "This is my test text"


if __name__ == '__main__':
    app.run(debug=True)
