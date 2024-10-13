"""
Custom types.
"""
from typing import TypeVar, Union
from app.models import Course, DemoEvent, Demo

# Any defined model.
ModelType = TypeVar("ModelType", bound=Union[Course, DemoEvent, Demo])
