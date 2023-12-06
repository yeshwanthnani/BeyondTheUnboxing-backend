from flask import Blueprint, jsonify, make_response
from models.model import Review, db, UserAccount, Mobile, Question
from flask import request
from models.Constants import HttpStatus, ResponseMessages
from DBLayer.ReviewHandler import ReviewHandler
from models.exceptions import Failed

"""-----------END POINTS----------:

create_review: POST     /api/v1/review/<int:user_id>/<int:mobile_id>/   (create a review)
get_reviews:   GET      /api/v1/review/<int:user_id>/<int:mobile_id>/   (to get the ratings given by a user for a mobile)
update_review: PUT      /api/v1/review/<int:user_id>/<int:mobile_id>/   (update existing rating)
Delete review: DELETE   /api/v1/review/<int:user_id>/<int:review_id>/   (to delete a particular review bsed on user_id and review_id)
"""

reviews_blueprint = Blueprint('reviews', __name__, url_prefix='/api/v1/')


@reviews_blueprint.route('review/<int:user_id>/<int:mobile_id>/', methods=['POST'])
def create_review(user_id, mobile_id):
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return make_response(jsonify({'error': ResponseMessages.UN_SUPPORTED_MEDIA_TYPE}),
                                 HttpStatus.UN_SUPPORTED_MEDIA_TYPE.value)

        # Getting json data from the request
        data = request.get_json()

        # Validation of required fields
        required_fields = ['question_ID', 'rating']

        for field in required_fields:
            if field not in data:
                return make_response((jsonify({'error': f'Missing required field: {field}'})),
                                     HttpStatus.BAD_REQUEST.value)

            # Check if mobile_ID exists in Mobile table
        if not Mobile.query.filter_by(mobile_ID=mobile_id).first():
            return make_response(jsonify({'error': 'Mobile ID does not exist'}), HttpStatus.NOT_FOUND.value)

            # Check if user_ID exists in UserAccount table
        if not UserAccount.query.filter_by(user_ID=user_id).first():
            return make_response(jsonify({'error': 'User ID does not exist'}), HttpStatus.NOT_FOUND.value)

            # Check if question_ID exists in Question table
        if not Question.query.filter_by(question_ID=data["question_ID"]).first():
            return make_response(jsonify({'error': 'Question ID does not exist'}), HttpStatus.NOT_FOUND.value)

        # Create a new Review instance for each question
        new_review = ReviewHandler.create_review(
            user_id,
            mobile_id,
            data["question_ID"],
            data["rating"]
        )
        response_data = {
            'message': ResponseMessages.CREATED.value,
            'review_ID': new_review.review_ID
        }
        return make_response(jsonify(response_data), HttpStatus.CREATED.value)
    except Failed as e:
        return make_response(jsonify({'error': e.message}), HttpStatus.BAD_REQUEST.value)




@reviews_blueprint.route('/review/<int:user_id>/<int:mobile_id>/', methods=['PUT'])
def update_review(user_id, mobile_id):
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return make_response(jsonify({'error': ResponseMessages.UN_SUPPORTED_MEDIA_TYPE}),
                                 HttpStatus.UN_SUPPORTED_MEDIA_TYPE.value)

        # Getting json data from the request
        data = request.get_json()

        # Validation of required fields
        required_fields = ["question_ID", 'rating']

        for field in required_fields:
            if field not in data:
                return make_response((jsonify({'error': f'Missing required field: {field}'})),
                                     HttpStatus.BAD_REQUEST.value)

        if not Mobile.query.filter_by(mobile_ID=mobile_id).first():
            return make_response(jsonify({'error': 'Mobile ID does not exist'}), HttpStatus.NOT_FOUND.value)

            # Check if user_ID exists in UserAccount table
        if not UserAccount.query.filter_by(user_ID=user_id).first():
            return make_response(jsonify({'error': 'User ID does not exist'}), HttpStatus.NOT_FOUND.value)

            # Check if question_ID exists in Question table
        if not Question.query.filter_by(question_ID=data["question_ID"]).first():
            return make_response(jsonify({'error': 'Question ID does not exist'}), HttpStatus.NOT_FOUND.value)

        review = ReviewHandler.update_review(
            user_id,
            mobile_id,
            data["question_ID"],
            data["rating"]
        )
        response_data = {
            'message': ResponseMessages.UPDATED.value,
            'rating': review.rating
        }
        return make_response(jsonify(response_data), HttpStatus.CREATED.value)
    except Failed as e:
        return make_response(jsonify({'error': e.message}), HttpStatus.BAD_REQUEST.value)




@reviews_blueprint.route('review/<int:user_id>/<int:mobile_id>/', methods=['GET'])
def get_reviews(user_id, mobile_id):
    try:
        if not Mobile.query.filter_by(mobile_ID=mobile_id).first():
            return make_response(jsonify({'error': 'Mobile ID does not exist'}), HttpStatus.NOT_FOUND.value)

            # Check if user_ID exists in UserAccount table
        if not UserAccount.query.filter_by(user_ID=user_id).first():
            return make_response(jsonify({'error': 'User ID does not exist'}), HttpStatus.NOT_FOUND.value)

        # Retrieve reviews based on user_id and mobile_id
        reviews = ReviewHandler.get_all_reviews(user_id, mobile_id)

        all_reviews = []

        if reviews:
            for every in reviews:
                review_data = {
                    'question_ID': every.question_ID,
                    'rating': every.rating,
                }
                all_reviews.append(review_data)

            return jsonify(all_reviews)
        else:
            return make_response(jsonify({'message': ResponseMessages.NOT_FOUND.value}), HttpStatus.NOT_FOUND.value)

    except Failed as e:
        return make_response(jsonify({'error': e.message}), HttpStatus.BAD_REQUEST.value)




@reviews_blueprint.route('review/<int:user_id>/<int:mobile_id>/', methods=['DELETE'])
def delete_reviews(user_id, mobile_id):
    try:
        if not Mobile.query.filter_by(mobile_ID=mobile_id).first():
            return make_response(jsonify({'error': 'Mobile ID does not exist'}), HttpStatus.NOT_FOUND.value)

            # Check if user_ID exists in UserAccount table
        if not UserAccount.query.filter_by(user_ID=user_id).first():
            return make_response(jsonify({'error': 'User ID does not exist'}), HttpStatus.NOT_FOUND.value)

        # Retrieve reviews based on user_id and mobile_id
        deleted_reviews = ReviewHandler.delete_reviews(user_id, mobile_id)
        if deleted_reviews:
            return make_response(jsonify({'message': ResponseMessages.SUCCESS.value}), HttpStatus.SUCCESS.value)
        else:
            return make_response(jsonify({'message': ResponseMessages.NOT_FOUND.value}), HttpStatus.NOT_FOUND.value)
    except Failed as e:
        return make_response(jsonify({'error': e.message}), HttpStatus.BAD_REQUEST.value)
