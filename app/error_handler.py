from marshmallow import ValidationError
from flask import jsonify, Flask


def handle_ma_validatin_error(e: ValidationError):
    return jsonify(e.messages), 422


def register_error_handlers(app: Flask):
    app.register_error_handler(ValidationError, handle_ma_validatin_error)
