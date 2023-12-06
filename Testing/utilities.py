
import json
import requests
from flask import Flask, jsonify
from sqlalchemy.exc import IntegrityError
from models.model import UserAccount,Question,Mobile,Review,db
from models.exceptions import UserAlreadyExists,QuestionAlreadyExists, MobileAlreadyExists
from models.Constants import MobileBrands, HttpStatus,ResponseMessages


app = Flask(__name__)

# Configure Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Nani8901@database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com/MyDataBase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def create_user(user_name, user_email, password, year_of_birth):
    with app.app_context():
        endpoint = "http://127.0.0.1:5000/api/v1/user/"
        user_data = {
            "user_name": user_name,
            "user_email": user_email,
            "password": password,
            "year_of_birth": year_of_birth
        }
        body = json.dumps(user_data)
        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url=endpoint, data=body, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error creating user: {e}")
            raise UserAlreadyExists()

        try:
            assert response.status_code == 201
            created_user = UserAccount.query.filter_by(user_name=user_name).first()
            return created_user
        except IntegrityError:
            db.session.rollback()
            print("Error: User with the same details already exists.")
            raise UserAlreadyExists()



def create_question(question_text):
    with app.app_context():
        endpoint = "http://127.0.0.1:5000/api/v1/question/"
        question_data = {
            "question_text": question_text
        }
        body = json.dumps(question_data)
        headers = {
            "Content-Type": "application/json"
        }


        try:
            response = requests.post(url=endpoint, data=body, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error Adding Question: {e}")
            raise QuestionAlreadyExists()

        try:
            assert response.status_code == 201
            added_question = Question.query.filter_by(question_text=question_text).first()
            return added_question
        except IntegrityError:
            db.session.rollback()
            print("Issue: Same question already exists.")
            raise QuestionAlreadyExists()




def create_mobile(brand, mobile_name):
    with app.app_context():
        endpoint = "http://127.0.0.1:5000/api/v1/mobile/"
        mobile_data = {
            "brand": brand,
            "mobile_name": mobile_name
        }
        body = json.dumps(mobile_data)
        headers = {
            "Content-Type": "application/json"
        }
        if mobile_data['brand'].upper() not in [brand.upper() for brand in MobileBrands.smartphones]:
            return jsonify({'error': 'Invalid Mobile Brand'}), HttpStatus.BAD_REQUEST

        try:
            response = requests.post(url=endpoint, data=body, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error creating mobile: {e}")
            raise MobileAlreadyExists()

        try:
            assert response.status_code == 201
            created_mobile = Mobile.query.filter_by(mobile_name=mobile_name).first()
            return created_mobile
        except IntegrityError:
            db.session.rollback()
            print("Error: Mobile with the same details already exists.")
            raise MobileAlreadyExists()


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


