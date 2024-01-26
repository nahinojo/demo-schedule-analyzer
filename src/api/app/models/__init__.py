from .Base import Base
from .Course import Course
from .Demo import Demo
from .DemoEvent import DemoEvent

from sqlalchemy import create_engine

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)