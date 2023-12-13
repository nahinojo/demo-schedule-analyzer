from flask import Flask, request, send_file, render_template
from utils.generate_schedule import generate_schedule, SCHEDULE_FILE_NAME

app = Flask(__name__)


@app.route('/new_schedule', methods=['GET'])
def new_schedule():
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
    return send_file(f"./build/{SCHEDULE_FILE_NAME}", as_attachment=True)


@app.route('/')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
