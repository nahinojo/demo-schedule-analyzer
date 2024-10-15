"""
Routes for the API.

"""
from flask import Blueprint, make_response

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/generate_schedule/<course_ids>', methods=['GET'])
def generate_schedule_route(course_ids):
    """
    Generates a demo schedule.

    Paramaters
    ----------
    course_ids: str
        The list of course ids.

    Returns
    -------
    response: dict
        The HTTP response message.
    """
    try:
        course_ids = [int(course_id) for course_id in course_ids.split(',')]
        generate_schedule(course_ids=course_ids)
    except Exception as e:
        message = {"status": "error", "message": str(e)}
        response = make_response(message, 500)
    else:
        message = {
            "status": "success",
            "message": "Schedule generated successfully."
        }
        response = make_response(message, 200)
    return response


@api_blueprint.route('/get_courses_table', methods=['GET'])
def get_courses_table_route():
    """
    Gets the list of all courses from the database for display.
    """
    try:
        course_table = get_courses_table()
    except Exception as e:
        message = {"status": "error", "message": str(e)}
        response = make_response(message, 500)
    else:
        message = {
            "status": "success",
            "message": "Course table retrieved successfully.",
            "data": course_table
        }
        response = make_response(message, 200)
    return response


@api_blueprint.route('/sandbox', methods=['GET'])
def sandbox():
    """
    Sandbox route.
    """
    status_code = 200

    return "Sandbox route successful!"
