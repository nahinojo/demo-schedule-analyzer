"""
The database models.
"""

import datetime
from typing import List

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    course_code: Mapped[str] = mapped_column(String(6))
    instructor: Mapped[str] = mapped_column(String)
    term: Mapped[str] = mapped_column(String(6))
    year: Mapped[int] = mapped_column(Integer)
    demo_events: Mapped[List["DemoEvent"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan"
        )

    def __repr__(self):
        return (f"Course(id={self.id!r}, "
                f"course_code={self.course_code!r}, "
                f"instructor={self.instructor!r}, "
                f"term={self.term!r}, "
                f"year={self.year!r})"
                )


class DemoEvent(Base):
    __tablename__ = "demo_events"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_date: Mapped[datetime.date] = mapped_column(Date)
    additional_information: Mapped[str] = mapped_column(String)
    demos: Mapped[List["Demo"]] = relationship(
        back_populates="demo_event",
        cascade="all, delete-orphan",
        uselist=True
        )
    course_id = mapped_column(ForeignKey("courses.id"), nullable=False)
    course: Mapped["Course"] = relationship(back_populates="demo_events")

    def __repr__(self):
        return (f"DemoEvent(id={self.id!r}, "
                f"event_date={self.event_date!r}, "
                f"additional_information={self.additional_information!r})"
                )


class Demo(Base):
    __tablename__ = "demos"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    demo_event_id = mapped_column(ForeignKey("demo_events.id"), nullable=False)
    demo_event: Mapped["DemoEvent"] = relationship(back_populates="demos")

    def __repr__(self):
        return (f"Demo(id={self.id!r}, "
                f"name={self.name!r})"
                )
