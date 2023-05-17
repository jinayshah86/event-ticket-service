from models import ma
from models.events import Event

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Event


create_event_schema: SQLAlchemyAutoSchema = EventSchema(exclude=("id", "created_at", "updated_at"))
update_event_schema: SQLAlchemyAutoSchema = EventSchema(
    exclude=("id", "created_at", "updated_at", "date", "availability")
)
event_schema: SQLAlchemyAutoSchema = EventSchema()
events_schema: SQLAlchemyAutoSchema = EventSchema(many=True)
