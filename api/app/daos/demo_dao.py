"""
Demo DAO.
"""
from app.models import Demo
from ._base_dao import _BaseDAO


class DemoDAO(_BaseDAO):
    """
    Demo Data Access Object (DAO).
    """
    _model_type = Demo
