from app.models import Base, DemoEvent

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped


class Demo(Base):
    __tablename__ = "demo"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    demo_event_id = mapped_column(ForeignKey("demo_event.id"))
    demo_event: Mapped["DemoEvent"] = relationship(back_populates="demos")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "demo_event_id": self.demo_event_id,
            "demo_event": self.demo_event.serialize()
        }
