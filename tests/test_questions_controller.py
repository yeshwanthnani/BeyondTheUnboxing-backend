from models.model import db, Question
from app import app
import json
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

def test_create_question(client, init_database):
    new_question_data = {
        "question_text": "This a question registered by post method"
    }
    response = client.post('/api/v1/question/register/', data=json.dumps(new_question_data), content_type='application/json')
    # check if response is correct

    assert response.status_code == 201
    assert 'question_ID' in response.json
    assert response.json["message"] == "New question entry created successfully"
    new_question_added = Question.query.filter_by(question_text='This a question registered by post method').first()
    assert new_question_added is not None
    assert new_question_added.question_ID is not None


def test_get_question1_by_ID(client, init_database, question_data_setup):
    test_question_1, test_question_2 = question_data_setup

    response1 = client.get(f'/api/v1/question/{test_question_1.question_ID}')
    assert response1.status_code == 200
    assert response1.json["question_text"] == "This is a test question_1"

def test_get_question2_by_ID(client, init_database, question_data_setup):
    test_question_1, test_question_2 = question_data_setup
    response2 = client.get(f'/api/v1/question/{test_question_2.question_ID}')
    assert response2.status_code == 200
    assert response2.json["question_text"] == "This is a test question_2"


def test_get_all_question_entries(client, init_database):
    response = client.get('api/v1/question/all/')
    assert response.status_code == 200