from flask_restful import Resource
from flask import session

class Logout(Resource):
    def delete(self):
        if session.get("user_id"):
            session.pop("user_id")
            return {}, 204
        return {'error': 'Unauthorized'}, 401 