import json
import requests
from flask import Flask
from sqlalchemy.exc import IntegrityError
from models.model import Mobile, db
from models.exceptions import MobileAlreadyExists
# Import the UserAccount model and db

app = Flask(__name__)

# Configure Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Nani8901@database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com/MyDataBase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


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