# controllers/overall_review_controller.py

from flask import Blueprint, jsonify, request, make_response
from models.model import db, UserOverAllReview, UserAccount, Mobile
from models.Constants import HttpStatus, ResponseMessages
from DBLayer.OverAllReviewHandler import OverAllReviewHandler
from models.exceptions import Failed

overall_review_controller = Blueprint('overall_review_controller', __name__, url_prefix='/api/v1/')


@overall_review_controller.route('review_comment/<int:user_id>/<int:mobile_id>/', methods=['POST'])
def create_overall_review(user_id, mobile_id):
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return make_response(jsonify({'error': ResponseMessages.UN_SUPPORTED_MEDIA_TYPE}),
                                 HttpStatus.UN_SUPPORTED_MEDIA_TYPE.value)

        # Getting json data from the request
        data = request.get_json()

        # Validation of required fields

        if 'review_comment' not in data:
            return make_response((jsonify({'error': f'Missing required field'})),
                                 HttpStatus.BAD_REQUEST.value)

        if not Mobile.query.filter_by(mobile_ID=mobile_id).first():
            return make_response(jsonify({'error': 'Mobile ID does not exist'}), HttpStatus.NOT_FOUND.value)

            # Check if user_ID exists in UserAccount table
        if not UserAccount.query.filter_by(user_ID=user_id).first():
            return make_response(jsonify({'error': 'User ID does not exist'}), HttpStatus.NOT_FOUND.value)

        comment = OverAllReviewHandler.add_comment(
            user_id,
            mobile_id,
            data['review_comment']
        )
        response_data = {
            'message': ResponseMessages.CREATED.value,
            'user_id': comment.user_ID,
            'mobile_ID': comment.mobile_ID,
            'review_comment_ID': comment.id
        }
        return make_response(jsonify(response_data), HttpStatus.CREATED.value)
    except Failed as e:
        return make_response(jsonify({"error": e.message}), HttpStatus.BAD_REQUEST.value)





@overall_review_controller.route('review_comment/<int:user_id>/<int:mobile_id>/', methods=['PUT'])
def update_overall_review(user_id, mobile_id):
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return make_response(jsonify({'error': ResponseMessages.UN_SUPPORTED_MEDIA_TYPE}),
                                 HttpStatus.UN_SUPPORTED_MEDIA_TYPE.value)

        # Getting json data from the request
        data = request.get_json()

        # Validation of required fields

        if 'review_comment' not in data:
            return make_response((jsonify({'error': f'Missing required field'})),
                                 HttpStatus.BAD_REQUEST.value)

        if not Mobile.query.filter_by(mobile_ID=mobile_id).first():
            return make_response(jsonify({'error': 'Mobile ID does not exist'}), HttpStatus.NOT_FOUND.value)

            # Check if user_ID exists in UserAccount table
        if not UserAccount.query.filter_by(user_ID=user_id).first():
            return make_response(jsonify({'error': 'User ID does not exist'}), HttpStatus.NOT_FOUND.value)

        comment = OverAllReviewHandler.update_comment(
            user_id,
            mobile_id,
            data['review_comment']
        )
        response_data = {
            'message': ResponseMessages.UPDATED.value,
            'user_id': comment.user_ID,
            'mobile_ID': comment.mobile_ID,
            'review_comment_ID': comment.id
        }
        return make_response(jsonify(response_data), HttpStatus.CREATED.value)
    except Failed as e:
        return make_response(jsonify({'error': e.message}), HttpStatus.BAD_REQUEST.value)


