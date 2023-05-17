from models import BaseModel
from sqlalchemy import String, DateTime, Column, Integer, CheckConstraint


class Event(BaseModel):
    __table_args__ = (
        CheckConstraint("availability >= 0", name="availability_non_negative"),
    )

    name = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)
    availability = Column(Integer, nullable=False)
