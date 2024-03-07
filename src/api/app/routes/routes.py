from flask import Blueprint, request
from app.utils import generate_schedule

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/generate_schedule', methods=['GET'])
def generate_schedule_route():
    # from app.database import Session
    # from app.database.setup_db import setup_db
    # from app.models import Course
    # from sqlalchemy import text, select, inspect
    # with Session() as session:
    #     setup_db()
    #     inspector = inspect(session)
    #     tables = inspector.get_table_names()
    #     print(tables)
    generate_schedule(
        target_course_code=request.args.get('target_course_code', None),
        target_instructor=request.args.get('target_instructor', None),
        target_term=request.args.get('target_term', None),
        target_year=int(request.args.get('target_year', 2020)),
        is_target_year_as_minium=request.args.get('is_target_year_as_minimum', True)
    )
