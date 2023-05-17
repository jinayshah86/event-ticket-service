from flask_restful import Api, abort


class CustomApi(Api):

    def handle_error(self, e: Exception):
        abort(e.code, str(e))
