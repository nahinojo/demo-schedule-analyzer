from datetime import date
from flask import Blueprint, request, jsonify
from sqlalchemy import text

from app.database import Session

from app.utils import generate_schedule, get_filtered_courses

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/generate_schedule', methods=['GET'])
def generate_schedule_route():
    """
    Generates an demo schedule.
    """
    is_target_year_as_minium = request.args.get('is_target_year_as_minimum', True)
    if type(is_target_year_as_minium) == str and is_target_year_as_minium.lower() == "false":
        is_target_year_as_minium = False
    generate_schedule(
        target_course_code=request.args.get('target_course_code', None),
        target_instructor=request.args.get('target_instructor', None),
        target_term=request.args.get('target_term', None),
        target_year=int(request.args.get('target_year', date.today().year)),
        is_target_year_as_minium=is_target_year_as_minium
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
    target_year = int(request.args.get('target_year', date.today().year))
    is_target_year_as_minimum = request.args.get('is_target_year_as_minimum', True)
    if type(is_target_year_as_minimum) == str and is_target_year_as_minimum.lower() == "false":
        is_target_year_as_minimum = False
    with Session() as session:
        courses = get_filtered_courses(
            session=session,
            target_course_code=target_course_code,
            target_instructor=target_instructor,
            target_term=target_term,
            target_year=target_year,
            is_target_year_as_minimum=is_target_year_as_minimum
        )
        attribute_options = {
            "course_code": target_course_code if target_course_code is not None else [],
            "instructor": target_instructor if target_instructor is not None else [],
            "term": target_term if target_term is not None else [],
            "year": target_year,
            "is_target_year_as_minimum": str(is_target_year_as_minimum)
        }
        for course in courses:
            if not target_course_code and course.course_code not in attribute_options["course_code"]:
                attribute_options["course_code"].append(course.course_code)
            if not target_instructor and course.instructor not in attribute_options["instructor"]:
                attribute_options["instructor"].append(course.instructor)
            if not target_term and course.term not in attribute_options["term"]:
                attribute_options["term"].append(course.term)
    return jsonify(attribute_options)
