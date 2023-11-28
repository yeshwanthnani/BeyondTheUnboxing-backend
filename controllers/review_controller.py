from flask import Blueprint, jsonify
from models.model import Review, db
from flask import request



# all urls  (user paths):
   # Get method: /api/v1/reviews/<int:user_id>/<int:mobile_id>   (to get the ratings given by a user for a mobile)
   # Post method: /api/v1/reviews/<int:user_id>/<int:mobile_id>  (to give the ratings by a user for a mobile)
   # Delete method: /api/v1/reviews/<int:user_id>/<int:review_id>   (to delete a particular review bsed on user_id and review_id)


reviews_blueprint = Blueprint('reviews', __name__, url_prefix='/api/v1/reviews')

@reviews_blueprint.route('/<int:user_id>/<int:mobile_id>', methods=['GET'])
def get_review(user_id, mobile_id):
    reviews = Review.query.filter_by(user_ID=user_id, mobile_ID=mobile_id).all()

    all_reviews=[]


    if reviews:
        for every in reviews:
            review_data = {

                'question_ID': every.question_ID,
                'rating': every.rating,
            }
            all_reviews.append(review_data)
    if all_reviews:
        return jsonify(all_reviews)
    else:
        return jsonify({'message': 'Review not found for the specified user and mobile'}), 404



@reviews_blueprint.route('/<int:user_id>/<int:mobile_id>', methods=['POST'])
def create_review(user_id, mobile_id):
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type'}), 415

        # Getting json data from the request
        data = request.get_json()

        # Validation of required fields
        required_fields = [f'{i}' for i in range(1,11)]

        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field : {field}'}), 400

        # Create a new Review instance for each question
        for i in range(1, 11):
            question_key = f'{i}'
            rating = data[question_key]

            new_review = Review(
                user_ID=user_id,
                mobile_ID=mobile_id,
                question_ID=i,
                rating=rating,
            )

            db.session.add(new_review)

        db.session.commit()

        return jsonify({'message': 'Reviews created successfully'}), 201

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500



@reviews_blueprint.route('/<int:user_id>/<int:review_id>', methods=['DELETE'])

def delete_review(user_id, review_id):

    try:
        review = Review.query.filter_by( user_ID =user_id, review_ID=review_id).first()


        if review:
            # Delete the review from the database
            db.session.delete(review)
            db.session.commit()

            return jsonify({'message': 'Review deleted successfully'}), 200

        else:
            return jsonify({'message': 'Review not found'}), 404

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500
