from models.model import Review, db
from models.exceptions import Failed


class ReviewHandler():

    def __init__(self):
        return

    @staticmethod
    def create_review(user_id, mobile_id, question_ID, rating):
        try:
            new_review = Review(
                user_ID=user_id,
                mobile_ID=mobile_id,
                question_ID=question_ID,
                rating=rating,
            )
            db.session.add(new_review)
            db.session.commit()
            return new_review
        except Exception as e:
            raise Failed()

    @staticmethod
    def update_review(user_id, mobile_id, question_ID, rating):
        try:
            review = Review.query.filter_by(user_ID=user_id, mobile_ID=mobile_id, question_ID=question_ID).first()
            if review:
                review.rating = rating
            db.session.commit()
            return review
        except Exception as e:
            raise Failed()



    @staticmethod
    def get_all_reviews(user_id, mobile_id):
        try:
            reviews = Review.query.filter_by(user_ID=user_id, mobile_ID=mobile_id).all()
            return reviews
        except Exception as e:
            raise Failed()

    @staticmethod
    def delete_reviews(user_id, mobile_id):
        try:
            delete = False
            # Fetch reviews based on user_id and mobile_id
            deleted_reviews = Review.query.filter_by(user_ID=user_id, mobile_ID=mobile_id).all()
            # Delete the fetched reviews
            for review in deleted_reviews:
                db.session.delete(review)
                delete = True
            # Commit the changes to the database
            db.session.commit()
            return delete
        except Exception as e:
            raise Failed()
