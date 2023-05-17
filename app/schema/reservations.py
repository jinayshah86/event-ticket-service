from models import ma
from models.reservations import Reservation

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class ReservationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reservation
        include_fk = True


create_reservation_schema: SQLAlchemyAutoSchema = ReservationSchema(
    exclude=("id", "created_at", "updated_at", "cancelled")
)
update_reservation_schema: SQLAlchemyAutoSchema = ReservationSchema(
    exclude=("id", "created_at", "updated_at", "cancelled", "event_id")
)
reservation_schema: SQLAlchemyAutoSchema = ReservationSchema()
reservations_schema: SQLAlchemyAutoSchema = ReservationSchema(many=True)
