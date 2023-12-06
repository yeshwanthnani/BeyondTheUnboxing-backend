import pytest
from models.model import Mobile, Question, db
import json
from app import app

from models.exceptions import UserAlreadyExists, MobileAlreadyExists
from models.Constants import HttpStatus,ResponseMessages
import pytest
from tests.create_questions import create_question
from models.exceptions import QuestionAlreadyExists



@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
@pytest.fixture()
def init_database(request):
    with app.app_context():
        def teardown():
            with app.app_context():
                db.session.query(Question).filter(Question.question_text.in_(['This is a test question_1',
                                                                              'This is a test question_2',
                                                                              'This a question registered by post method'])).delete()
                db.session.commit()

            # Add the teardown function as a finalizer
        request.addfinalizer(teardown)
        yield db
        # Commit the changes
        db.session.commit()




@pytest.fixture()
def question_data_setup():
    test_question_1 = create_question(question_text="This is a test question_1")
    test_question_2 = create_question(question_text="This is a test question_2")
    return test_question_1, test_question_2

