from flask import Blueprint, jsonify, request, make_response
from models.Constants import HttpStatus, ResponseMessages
from models.exceptions import UserAlreadyExists, UserDoesNotExist
from DBLayer.UserAccountHandler import UserAccountHandler

user_blueprint = Blueprint('user', __name__, url_prefix='/api/v1/')

"""-------------------ENDPOINTS---------------"""



@user_blueprint.route('user/', methods=['POST'])
def create_user():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate required fields
        required_fields = ['user_name', 'user_email', 'password', 'year_of_birth']
        for field in required_fields:
            if field not in data:
                return make_response(jsonify({'error': f'Missing required field: {field}'}), HttpStatus.BAD_REQUEST.value)

        # Call create_user method from UserAccountHandler
        new_user = UserAccountHandler.create_user(
            data['user_name'],
            data['user_email'],
            data['password'],
            data['year_of_birth']
        )
        # Return a success response
        response_data = {
            'message': ResponseMessages.CREATED.value,
            'data': {
                'user_name': new_user.user_name,
                'user_email': new_user.user_email,
                'user_ID': new_user.user_ID
            }
        }
        return make_response(jsonify(response_data), HttpStatus.CREATED.value)
    except UserAlreadyExists as e:
        # Handle other potential exceptions
        return make_response(jsonify({"error": e.message}), HttpStatus.BAD_REQUEST.value)



@user_blueprint.route('user/<int:user_ID>', methods=['GET'])
def get_user(user_ID):
    try:
        user = UserAccountHandler.get_user_details(user_ID)
        return make_response(jsonify(user), HttpStatus.SUCCESS.value)
    except UserDoesNotExist as e:
        return make_response(jsonify({"error": e.message}), HttpStatus.BAD_REQUEST.value)




@user_blueprint.route('user/<int:user_ID>', methods=['DELETE'])
def delete_user(user_ID):
    try:
        UserAccountHandler.delete_user(user_ID)
        return make_response(jsonify({'message': ResponseMessages.SUCCESS}), HttpStatus.SUCCESS.value)
    except UserDoesNotExist as e:
        return make_response(jsonify({"error": e.message}), HttpStatus.NOT_FOUND.value)







