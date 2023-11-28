from models.model import db
from app import app
from models.model import UserAccount
import json
import pytest

@pytest.fixture

def client():
    with app.test_client() as client:
        yield client

@pytest.fixture()
def init_database():
    with app.app_context():
        db.create_all()
        yield db
        UserAccount.query.delete()

        # Commit the changes
        db.session.commit()


def test_get_user(client, init_database):

    # Create a test user in the database
    test_user = UserAccount(user_name='TestUser', user_email = 'test@gmail.com', password = "testpassword", year_of_birth = 1990)
    init_database.session.add(test_user)
    init_database.session.commit()

    # Send a GET request to retrieve the user
    response = client.get(f'/api/v1/user/{test_user.user_ID}')

    #checking if response is successfull
    assert response.status_code == 200

    # Check if the returned data matches the test user's data

    assert response.json['user_name'] == 'TestUser'
    assert response.json['user_email'] == 'test@gmail.com'
    assert response.json['year_of_birth'] == 1990


def test_create_user(client, init_database):
    # Data for creating a new user
    new_user_data = {
        'user_name': 'NewUser',
        'user_email': 'newuser@example.com',
        'password': 'newpassword',
        'year_of_birth': 1995
    }

    # Send a POST request to create a new user
    response = client.post('/api/v1/user/', data=json.dumps(new_user_data), content_type='application/json')

    # Check if the response is successful
    assert response.status_code == 201

    # Check if the returned data contains the user_ID and message
    assert 'user_ID' in response.json
    assert response.json['message'] == 'User created successfully'

    # Check if the user is added to the database
    new_user = UserAccount.query.filter_by(user_name='NewUser').first()
    assert new_user is not None
    assert new_user.user_email == 'newuser@example.com'
    assert new_user.year_of_birth == 1995



