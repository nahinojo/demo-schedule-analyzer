from flask import Blueprint, request

from app.database import Session
from app.models import Course
from app.utils import generate_schedule

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/generate_schedule', methods=['GET'])
def generate_schedule_route():
    """
    Generates an demo schedule.
    """
    print("GENERATING SCHEDULE")
    print(request.args)
    generate_schedule(
        target_course_code=request.args.get('target_course_code', None),
        target_instructor=request.args.get('target_instructor', None),
        target_term=request.args.get('target_term', None),
        target_year=int(request.args.get('target_year', 2020)),
        is_target_year_as_minium=request.args.get('is_target_year_as_minimum', True)
    )
    return "SCHEDULE GENERATED"

@api_blueprint.route('/course_attribute_options', methods=['GET'])
def course_attribute_options_route():
    """
    Gets all the possible course attribute options within the scope of the provided attributes.
    """
    target_course_code = request.args.get('target_course_code', None)
    target_instructor = request.args.get('target_instructor', None)
    target_term = request.args.get('target_term', None)
    target_year = int(request.args.get('target_year', 2020))
    is_target_year_as_minimum = request.args.get('is_target_year_as_minimum', True)

    course_codes = set(target_course_code)
    instructors = set(target_instructor)
    terms = set(target_term)
    years = set(target_year)

    with Session() as session:
        for course in session.get(Course):
            course_code = course.course_code
            instructor = course.instructor
            term = course.term
            year = course.year

    return {
        "course_code": list(course_codes),
        "instructor": list(instructors),
        "term": list(terms),
        "year": list(years)
    }
