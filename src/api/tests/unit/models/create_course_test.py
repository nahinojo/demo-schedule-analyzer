from app.database import Session
# from app.models import Course

import pytest
from sqlalchemy import select

from typing import List
# from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class DemoEvent(Base):
    __tablename__ = "demo_event"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_date: Mapped[Date] = mapped_column(Date)
    additional_info: Mapped[str] = mapped_column(String)
    # demos: Mapped[List["Demo"]] = relationship(back_populates="demo_event")
    course_id = mapped_column(ForeignKey("course.id"))
    course: Mapped["Course"] = relationship(back_populates="demo_events")

    def serialize(self):
        return {
            "id": self.id,
            "event_date": self.event_date,
            "additional_info": self.additional_info,
            # "demos": [demo.serialize() for demo in self.demos],
            "course_id": self.course_id
        }


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


@pytest.mark.usefixtures("app_context")
def create_course_test():
    with Session() as session:
        print("test")
        course = Course(
            course_code="COURSE_CODE_TEST",
            instructor="INSTRUCTOR_TEST",
            term="TERM_TEST",
        )
        session.add(course)
        session.commit()
        stmt = select(Course).where(Course.id == 0)
        result_course = session.execute(stmt)
        print(result_course.scalar())
        assert False
