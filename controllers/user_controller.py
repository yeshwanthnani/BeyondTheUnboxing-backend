from flask import Blueprint, jsonify
from models.model import UserAccount

user_blueprint = Blueprint('user', __name__, url_prefix='/api/v1/UserAccount/{user_ID}')

@user_blueprint.route('/<int:user_ID>', methods=['GET'])
def get_user(user_ID):
    user = UserAccount.query.get(user_ID)
    if user:
        user_data = {
            'user_ID': user.user_ID,
            'user_name': user.user_name,
            'user_email': user.user_email,
            'year_of_birth': user.year_of_birth,
            'created_on': user.created_on
        }
        return jsonify(user_data)
    else:
        return jsonify({'message': 'User not found'}), 404
