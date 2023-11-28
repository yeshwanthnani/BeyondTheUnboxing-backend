from flask import Blueprint, jsonify
from models.model import Mobile, db
from flask import request

mobile_blueprint = Blueprint('mobile', __name__, url_prefix='/api/v1/mobile')

# Url paths
#       GET  (/api/v1/mobile/<int:mobile_id>)  (to get details of a mobile)
#       POST (/api/v1/mobile/)                 to register or enter new mobile details into the table)


@mobile_blueprint.route('/<int:mobile_id>', methods=['GET'])
def get_mobile(mobile_id):
    mob = Mobile.query.get(mobile_id)


    if mob:
        mobile_data = {
            'mobile_ID': mob.mobile_ID,
            'brand': mob.brand,
            'mobile_name': mob.mobile_name,
            'created_on': mob.created_on,
        }

        return jsonify(mobile_data)
    else:
        return jsonify({'message': 'Mobile not found'}), 404

@mobile_blueprint.route('/', methods=['GET'])
def get_all_mobiles():
    mobiles = Mobile.query.all()

    mobiles_data=[]

    if mobiles:

        for mob in mobiles:
            mobile_data = {
                'mobile_ID': mob.mobile_ID,
                'brand': mob.brand,
                'mobile_name': mob.mobile_name,
                'created_on': mob.created_on,
            }
            mobiles_data.append(mobile_data)

        return jsonify(mobiles_data)
    else:
        return jsonify({'message': 'Mobile not found'}), 404


@mobile_blueprint.route('/',methods=['POST'])
def create_mobile():
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type'}), 415

        print(request)
        # Get JSON data from the request
        data = request.get_json()



        # Validate required fields
        required_fields = ['brand','mobile_name']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400



        # Create a new user instance
        new_mobile = Mobile(
            brand = data['brand'],
            mobile_name = data['mobile_name']
        )

        db.session.add(new_mobile)
        db.session.commit()

        # Return a success response
        response_data = {
            'message': 'New mobile entry created successfully',
            'mobile_ID': new_mobile.mobile_ID
        }
        return jsonify(response_data), 201

    except Exception as e:

        # Handle other potential exceptions
        return jsonify({'error': str(e)}), 500