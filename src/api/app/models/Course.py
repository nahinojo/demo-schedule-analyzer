from app.models import Base, DemoEvent

from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship, Mapped


class Course(Base):
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(primary_key=True)
    course_code: Mapped[str] = mapped_column(String(6))
    instructor: Mapped[str] = mapped_column(String)
    term: Mapped[str] = mapped_column(String(6))
    # year: Mapped[int] = mapped_column(Integer)
    demo_events: Mapped[List["DemoEvent"]] = relationship(
        back_populates="course",
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
