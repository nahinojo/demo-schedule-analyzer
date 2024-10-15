"""
Custom types.
"""
from typing import TypeVar, Union
from app.models import Course, DemoEvent, Demo, Schedule

# Used in _BaseDAO as generic database model type.
ModelType = TypeVar("ModelType",
                    bound=Union[Course, DemoEvent, Demo, Schedule]
                    )
