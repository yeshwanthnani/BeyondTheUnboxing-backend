import json
import requests
from flask import Flask
from sqlalchemy.exc import IntegrityError
from models.model import Question, db
from models.exceptions import QuestionAlreadyExists
# Import the UserAccount model and db

app = Flask(__name__)

# Configure Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Nani8901@database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com/MyDataBase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def create_question(question_text):
    with app.app_context():
        endpoint = "http://127.0.0.1:5000/api/v1/question/register/"
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