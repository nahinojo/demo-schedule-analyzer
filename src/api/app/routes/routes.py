from datetime import date

from flask import Blueprint, request, make_response
from app.utils import generate_schedule
from app.utils.calendar_to_xlsx.generate_schedule import generate_schedule


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/generate_schedule/<course_ids>', methods=['GET'])
def generate_schedule_route(course_ids):
    """
    Generates a demo schedule.

    Paramaters
    ----------
    course_ids: str
        The list of course ids.
    """
    try:
        course_ids = [int(course_id) for course_id in course_ids.split(',')]
        generate_schedule(course_ids=course_ids)
    except Exception as e:
        message = {"status": "error", "message": str(e)}
        response = make_response(message, 500)
    else:
        message = {"status": "success", "message": "Schedule generated successfully."}
        response = make_response(message, 200)
    return response
