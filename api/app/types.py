"""
Custom types.
"""
from typing import TypeVar, Union
from app.models import Course, DemoEvent, Demo

ModelType = TypeVar("ModelType", bound=Union[Course, DemoEvent, Demo])

