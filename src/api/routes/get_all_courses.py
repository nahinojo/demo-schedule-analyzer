from models import Course, db
from flask import jsonify


def get_all_courses():
    print("Getting courses...")
    result = db.session.execute(db.select(Course)).scalars().all()
    print("result:", result)
    return jsonify(result[0].serialize())
