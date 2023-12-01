# create_user.py

import json
import requests
from flask import Flask
from sqlalchemy.exc import IntegrityError
from models.model import UserAccount, db
from models.exceptions import UserAlreadyExists
# Import the UserAccount model and db

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

        # response = requests.post(url=endpoint, data=body, headers=headers)
        # assert response.status_code == 201
        # created_user = UserAccount.query.filter_by(user_name=user_name).first()
        # return created_user

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