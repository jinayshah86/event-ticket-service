from sqlalchemy import Column, Integer, CheckConstraint, Boolean

from models import db, BaseModel
from models.events import Event


class Reservation(BaseModel):
    __table_args__ = (
        CheckConstraint("no_of_tickets >= 0", name="no_of_tickets_non_negative"),
    )

    event_id = Column(db.ForeignKey(Event.id), nullable=False)
    event = db.relationship(Event, backref=db.backref("reservations"))
    no_of_tickets = Column(Integer, nullable=False)
    cancelled = Column(Boolean, default=False)
