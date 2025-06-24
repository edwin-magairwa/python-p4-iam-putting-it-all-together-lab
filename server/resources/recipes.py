from flask_restful import Resource
from flask import request, session
from models import Recipe, db

class RecipeIndex(Resource):
    def get(self):
        if user_id := session.get('user_id'):
            recipes = Recipe.query.filter_by(user_id=user_id).all()
            return [{
                'id': r.id,
                'title': r.title,
                'instructions': r.instructions,
                'minutes_to_complete': r.minutes_to_complete,
                'user': {
                    'id': r.user.id,
                    'username': r.user.username
                }
            } for r in recipes], 200
        return {'error': 'Unauthorized'}, 401

    def post(self):
        if user_id := session.get('user_id'):
            data = request.get_json()
            try:
                new_recipe = Recipe(
                    title=data['title'],
                    instructions=data['instructions'],
                    minutes_to_complete=data['minutes_to_complete'],
                    user_id=user_id
                )
                db.session.add(new_recipe)
                db.session.commit()
                return {
                    'id': new_recipe.id,
                    'title': new_recipe.title,
                    'instructions': new_recipe.instructions,
                    'minutes_to_complete': new_recipe.minutes_to_complete,
                    'user': {
                        'id': new_recipe.user.id,
                        'username': new_recipe.user.username
                    }
                }, 201
            except Exception as e:
                return {'errors': [str(e)]}, 422
        return {'error': 'Unauthorized'}, 401 