from app.models import Base, Course, Demo

from typing import List
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped


class DemoEvent(Base):
    __tablename__ = "demo_event"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_date: Mapped[Date] = mapped_column(Date)
    additional_info: Mapped[str] = mapped_column(String)
    demos: Mapped[List["Demo"]] = relationship(back_populates="demo_event")
    course_id = mapped_column(ForeignKey("course.id"))
    course: Mapped["Course"] = relationship(back_populates="demo_event")

    def serialize(self):
        return {
            "id": self.id,
            "event_date": self.event_date,
            "additional_info": self.additional_info,
            "demos": [demo.serialize() for demo in self.demos],
            "course_id": self.course_id
        }
