from flask import Blueprint, jsonify, request, make_response
from models.model import Mobile, db
from models.Constants import HttpStatus, ResponseMessages, MobileBrands
from flask import request
from DBLayer.MobileHandler import MobileHandler
from psycopg2.errors import IntegrityError
from models.exceptions import MobileDoesNotExists, MobileBrandDoesNotExists,MobileAlreadyExists

mobile_blueprint = Blueprint('mobile', __name__, url_prefix='/api/v1/mobile')





@mobile_blueprint.route('/', methods=['POST'])
def create_mobile():
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type'}), HttpStatus.UN_SUPPORTED_MEDIA_TYPE
        # Get JSON data from the request
        data = request.get_json()

        required_fields = ['brand', 'mobile_name']

        for field in required_fields:
            if field not in data:
                return make_response(jsonify({'error': f'Missing required field: {field}'}), HttpStatus.BAD_REQUEST.value)
        brands_list = [name.value for name in MobileBrands]

        if data['brand'].upper() not in brands_list:
            raise MobileBrandDoesNotExists()
        new_mobile = MobileHandler.create_mobile(
            data['brand'],
            data['mobile_name']
        )
        # Return a success response with the newly created mobile details
        response_data = {
            'message': ResponseMessages.CREATED.value,
            'mobile_id': new_mobile.mobile_ID,
            'brand': new_mobile.brand,
            'mobile_name': new_mobile.mobile_name,
        }
        return make_response(jsonify(response_data), HttpStatus.CREATED.value)
    except MobileBrandDoesNotExists as e:
        return make_response(jsonify({"error": e.message}), HttpStatus.INTERNAL_SERVER_ERROR.value)
    except MobileAlreadyExists as e:  # Replace with the actual exception you want to catch
        # Handle specific exceptions
        return make_response(jsonify({'error': e.message}), HttpStatus.INTERNAL_SERVER_ERROR.value)



@mobile_blueprint.route('/<int:mobile_id>', methods=['GET'])
def get_mobile(mobile_id):

    try:
        mobile = MobileHandler.get_mobile(mobile_id)
        return make_response(jsonify(mobile), HttpStatus.SUCCESS.value)
    except MobileDoesNotExists as e:
        return make_response(jsonify({"error": e.message}), HttpStatus.BAD_REQUEST.value)


@mobile_blueprint.route('/all/', methods=['GET'])
def get_all_mobiles():
    mobiles = Mobile.query.all()

    mobiles_data = []

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
        return jsonify({'message': 'Mobile not found'}), HttpStatus.NOT_FOUND
