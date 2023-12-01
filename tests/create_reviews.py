# create user review through post method , into the review table"


import json
import requests
from flask import Flask
from sqlalchemy.exc import IntegrityError
from models.model import Review , Mobile, UserAccount,Question, db
from tests import test_review_controller

# Import the UserAccount model and db

app = Flask(__name__)

# Configure Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Nani8901@database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com/MyDataBase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def create_user_review(existing_user_id, existing_mobile_id, rating_data):

    with app.app_context():
        user_exists = UserAccount.query.filter_by(user_ID=existing_user_id).first()
        mobile_exists = Mobile.query.filter_by(mobile_ID=existing_mobile_id).first()

        if not user_exists:
            raise ValueError(f"User with ID {existing_user_id} not found.")
        if not mobile_exists:
            raise ValueError(f"Mobile with ID {existing_mobile_id} not found.")


        # Loop through the 10 questions and insert reviews
        for i, rating in enumerate(rating_data, start=1):
            new_review = Review(
                user_ID=existing_user_id,
                mobile_ID=existing_mobile_id,
                question_ID=i,
                rating=rating,
            )
            db.session.add(new_review)

        db.session.commit()


if __name__ == "__main__":
    # Replace these values with the actual user and mobile IDs
    user_id = 1  # Replace with the actual user ID
    mobile_id = 1  # Replace with the actual mobile ID
    rating_data = [1, 2, 4, 5, 3, 4, 5, 3, 4, 1]

    create_user_review(existing_user_id=1, existing_mobile_id=1, *rating_data)