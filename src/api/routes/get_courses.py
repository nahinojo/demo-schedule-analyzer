from models import Course, db
from flask import jsonify

# Gets all courses, using the complicated execute-select format
# See TODO.md

def get_course():
    print("get_courses()...")
    result = db.session.get(Course, 1)
    if not result:
        return {"message": "No result found"}, 404
    course_code = result.course_code
    print("course_code:", course_code)
    return {"message": "success"}, 200
