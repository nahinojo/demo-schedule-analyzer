from models import Course, Demo, DemoEvent, db

from datetime import date
from flask import request


# Adding courses does not need to be API routes.
# Instead, try just making some method that adds a course to the db.
def add_course():
    # Delete all this!
    course_code = request.args.get('course_code')
    instructor = ""
    return {"status": "success", "message": "add_course() resolved successfully"}, 200
