from flask import Flask
from flask_cors import CORS

from loadenv import loadenv
from resources import hello
from error_handler import register_error_handlers


def create_app() -> Flask:
    loadenv()
    app = Flask(__name__)
    app.config.from_prefixed_env()
    CORS(app)
    # register blueprint here
    app.register_blueprint(hello.bp)
    # error handlers
    register_error_handlers(app)
    return app
