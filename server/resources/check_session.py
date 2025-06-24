from flask_restful import Resource
from flask import session
from models import User

class CheckSession(Resource):
    def get(self):
        if user_id := session.get("user_id"):
            user = User.query.get(user_id)
            if user:
                return {
                    'id': user.id,
                    'username': user.username,
                    'image_url': user.image_url,
                    'bio': user.bio
                }, 200
        return {'error': 'Unauthorized'}, 401 