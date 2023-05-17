from uuid import uuid4

from flask import Blueprint, request
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError

from models import db
from models.events import Event
from models.reservations import Reservation
from schema.reservations import reservations_schema, create_reservation_schema, update_reservation_schema, reservation_schema

bp = Blueprint("reservations", __name__, url_prefix="/reservations")
api = Api(bp)


class ListCreateAPIResource(Resource):
    def get(self):
        result = db.paginate(db.select(Reservation))
        return reservations_schema.dump(result), 200

    def post(self):
        data = request.json
        parsed_data = create_reservation_schema.load(data)
        obj = Reservation(**parsed_data)
        # Check whether event exists or not
        db.get_or_404(Event, obj.event_id, description=f"Event with event id: {obj.event_id} doesn't exist.")
        db.session.add(obj)
        # Update availability in event
        try:
            db.session.query(Event).filter_by(id=obj.event_id)\
                .update({"availability": Event.availability - obj.no_of_tickets})
        except IntegrityError:
            return {"error": "Requested number of tickets are not available."}, 400
        db.session.commit()
        return reservation_schema.dump(obj), 201


class RetrieveUpdateDestroyAPIResource(Resource):
    def get(self, reservation_id: uuid4):
        reservation = db.get_or_404(
            Reservation,
            reservation_id,
            description=f"Reservation with reservation id: {reservation_id} doesn't exist.",
        )
        return reservation_schema.dump(reservation), 201

    def patch(self, reservation_id: uuid4):
        reservation = db.get_or_404(
            Reservation,
            reservation_id,
            description=f"Reservation with reservation id: {reservation_id} doesn't exist.",
        )
        if reservation.cancelled:
            return {"error": "Cannot update cancelled reservation."}, 400
        update_data = update_reservation_schema.load(request.json, partial=True)
        tickets_diff = 0
        for key, val in update_data.items():
            if key == "no_of_tickets":
                tickets_diff = val - reservation.no_of_tickets
            setattr(reservation, key, val)

        # Update availability in event
        if tickets_diff:
            try:
                db.session.query(Event).filter_by(id=reservation.event_id) \
                    .update({"availability": Event.availability - tickets_diff})
            except IntegrityError:
                return {"error": "Requested number of tickets are not available."}, 400
        db.session.add(reservation)
        db.session.commit()
        return reservation_schema.dump(reservation), 200

    def delete(self, reservation_id: uuid4):
        reservation = db.get_or_404(
            Reservation,
            reservation_id,
            description=f"Reservation with reservation id: {reservation_id} doesn't exist.",
        )
        reservation.cancelled = True
        # Update availability in event
        db.session.query(Event).filter_by(id=reservation.event_id) \
            .update({"availability": Event.availability + reservation.no_of_tickets})
        db.session.add(reservation)
        db.session.commit()
        return {}, 204


api.add_resource(RetrieveUpdateDestroyAPIResource, "/<uuid:reservation_id>")
api.add_resource(ListCreateAPIResource, "/")
