from uuid import uuid4

from flask import Blueprint, request
from flask_restful import Api, Resource

from models import db
from models.events import Event
from schema.events import events_schema, create_event_schema, update_event_schema, event_schema

bp = Blueprint("events", __name__, url_prefix="/events")
api = Api(bp)


class ListCreateAPIResource(Resource):
    def get(self):
        result = db.paginate(db.select(Event))
        return events_schema.dump(result), 200

    def post(self):
        data = request.json
        parsed_data = create_event_schema.load(data)
        obj = Event(**parsed_data)
        db.session.add(obj)
        db.session.commit()
        return event_schema.dump(obj), 201


class RetrieveUpdateDestroyAPIResource(Resource):
    def get(self, event_id: uuid4):
        event = db.get_or_404(Event, event_id, description=f"Event with event id: {event_id} doesn't exist.")
        return event_schema.dump(event), 201

    def patch(self, event_id: uuid4):
        event = db.get_or_404(Event, event_id, description=f"Event with event id: {event_id} doesn't exist.")
        update_data = update_event_schema.load(request.json, partial=True)
        for key, val in update_data.items():
            setattr(event, key, val)
        db.session.add(event)
        db.session.commit()
        return event_schema.dump(event), 200

    def delete(self, event_id: uuid4):
        event = db.get_or_404(Event, event_id, description=f"Event with event id: {event_id} doesn't exist.")
        db.session.delete(event)
        db.session.commit()
        return {}, 204


api.add_resource(RetrieveUpdateDestroyAPIResource, "/<uuid:event_id>")
api.add_resource(ListCreateAPIResource, "/")
