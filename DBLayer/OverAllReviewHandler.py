from models.model import UserOverAllReview, db
from sqlalchemy.exc import IntegrityError
from models.exceptions import Failed


class OverAllReviewHandler():

    def __init__(self):
        return

    @staticmethod
    def add_comment(user_id, mobile_id, review_comment):
        try:
            comm = UserOverAllReview(
                user_ID=user_id,
                mobile_ID=mobile_id,
                review_comment=review_comment
            )
            db.session.add(comm)
            db.session.commit()
            return comm
        except Exception as e:
            raise Failed()


    @staticmethod
    def update_comment(user_id, mobile_id, review_comment):
        try:
            updated_comm = UserOverAllReview.query.filter_by(user_ID=user_id, mobile_ID=mobile_id).first()
            if updated_comm:
                updated_comm.review_comment = review_comment
            db.session.commit()
            return updated_comm
        except Exception as e:
            raise Failed()


