from flask import Blueprint
from flask_restful import Api, Resource

bp = Blueprint("hello", __name__, url_prefix="")
api = Api(bp)


class Hello(Resource):
    def get(self):
        return {"hello": "world"}


api.add_resource(Hello, "/")
