from flask import Blueprint, jsonify
from models.model import UserAccount, db
from flask import request

user_blueprint = Blueprint('user', __name__, url_prefix='/api/v1/user')

# all urls  (user paths):
   # Get method: /api/v1/user/<int:user_id>   (to get details of a single user)
   # Post method: /api/v1/user/               (to enter user details into the user table)


@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserAccount.query.get(user_id)

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

@user_blueprint.route('/', methods=['POST'])
def create_user():
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type'}), 415

        print(request)
        # Get JSON data from the request
        data = request.get_json()

        # Validate required fields
        required_fields = ['user_name', 'user_email', 'password', 'year_of_birth']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Create a new user instance
        new_user = UserAccount(
            user_name=data['user_name'],
            user_email=data['user_email'],
            password=data['password'],
            year_of_birth=data['year_of_birth']
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Return a success response
        response_data = {
            'message': 'User created successfully',
            'user_ID': new_user.user_ID
        }
        return jsonify(response_data), 201

    except Exception as e:
        # Handle other potential exceptions
        return jsonify({'error': str(e)}), 500




