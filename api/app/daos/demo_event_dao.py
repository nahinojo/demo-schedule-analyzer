"""
DemoEvent DAO.
"""
from app.models import DemoEvent
from ._base_dao import _BaseDAO


class DemoEventDAO(_BaseDAO):
    """
    DemoEvent DAO.
    """
    _model_type = DemoEvent
