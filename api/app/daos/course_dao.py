"""
Course Data Access Object (DAO).
"""
from app.models import Course
from ._base_dao import _BaseDAO


class CourseDAO(_BaseDAO):
    """
    Course Data Access Object (DAO).
    """
    _model_type = Course
