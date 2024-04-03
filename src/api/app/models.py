from typing import List

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Course(Base):
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(primary_key=True)
    course_code: Mapped[str] = mapped_column(String(6))
    instructor: Mapped[str] = mapped_column(String)
    term: Mapped[str] = mapped_column(String(6))
    year: Mapped[int] = mapped_column(Integer)
    demo_events: Mapped[List["DemoEvent"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan"
    )

    def serialize(self):
        return {
            "id": self.id,
            "course_code": self.course_code,
            "instructor": self.instructor,
            "term": self.term,
            "year": self.year,
            "demo_events": [demo_event.serialize() for demo_event in self.demo_events]
        }


class DemoEvent(Base):
    __tablename__ = "demo_event"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_date: Mapped[Date] = mapped_column(Date)
    additional_information: Mapped[str] = mapped_column(String)
    demos: Mapped[List["Demo"]] = relationship(
        back_populates="demo_event",
        cascade="all, delete-orphan"
    )
    course_id = mapped_column(ForeignKey("course.id"))
    course: Mapped["Course"] = relationship(back_populates="demo_events")

    def serialize(self):
        return {
            "id": self.id,
            "event_date": self.event_date,
            "additional_information": self.additional_information,
            "demos": [demo.serialize() for demo in self.demos]
        }


class Demo(Base):
    __tablename__ = "demo"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    demo_event_id = mapped_column(ForeignKey("demo_event.id"))
    demo_event: Mapped["DemoEvent"] = relationship(back_populates="demos")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
