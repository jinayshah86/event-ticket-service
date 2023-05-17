from flask import Flask
from flask_cors import CORS

from loadenv import loadenv
from models import db, ma, migrate
from resources import hello, events
from error_handler import register_error_handlers


def create_app() -> Flask:
    loadenv()
    app = Flask(__name__)
    app.config.from_prefixed_env()
    CORS(app)
    # initialize db, migrate, and marshmallow
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    # register blueprint here
    app.register_blueprint(hello.bp)
    app.register_blueprint(events.bp)
    # error handlers
    register_error_handlers(app)
    return app
