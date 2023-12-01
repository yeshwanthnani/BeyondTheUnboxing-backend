from models.model import db, UserAccount, Mobile
from app import app
import json
import pytest
from sqlalchemy.exc import IntegrityError

from tests.create_user import create_user
from tests.create_mobile import create_mobile
from models.exceptions import UserAlreadyExists, MobileAlreadyExists

@pytest.fixture

def client():
    with app.test_client() as client:
        yield client

@pytest.fixture()
def init_database(request):
    with app.app_context():
        def teardown():
            with app.app_context():
                db.session.query(UserAccount).filter(UserAccount.user_name.in_(['kranthi', 'yesh', 'NewUser'])).delete()
                db.session.commit()

            # Add the teardown function as a finalizer
        request.addfinalizer(teardown)
        yield db
        # Commit the changes
        db.session.commit()

@pytest.fixture()
def user_setup():
    test_user1 = create_user(user_name="kranthi", user_email="Kranthi@gmail.com", password="HJKLIJ@90", year_of_birth=1997)
    test_user2 = create_user(user_name="yesh", user_email="Yesh@gmail.com", password="7545fdygJ@90", year_of_birth=1997)
    # test_user3 = create_user(user_name="yesh", user_email="Yesh@gmail.com", password="7545fdygJ@90", year_of_birth=1997)
    return test_user1, test_user2



def test_get_user(client, init_database, user_setup):
    test_user1, test_user2 = user_setup
    # Send a GET request to retrieve the user
    response = client.get(f'/api/v1/user/{test_user1.user_ID}')
    # Checking if response is successful
    assert response.status_code == 200

def test_check_response_of_test_user1(client, init_database, user_setup):
    test_user1, test_user2 = user_setup
    # Check if the returned data matches the test user's data
    response = client.get(f'/api/v1/user/{test_user1.user_ID}')
    assert response.json['user_name'] == 'kranthi'
    assert response.json['user_email'] == 'Kranthi@gmail.com'
    assert response.json['year_of_birth'] == 1997

def test_check_response_of_test_user2(client, init_database, user_setup):
    test_user1, test_user2 = user_setup
    # Check if the returned data matches the test user's data
    response = client.get(f'/api/v1/user/{test_user2.user_ID}')
    assert response.json['user_name'] == 'yesh'
    assert response.json['user_email'] == 'Yesh@gmail.com'
    assert response.json['year_of_birth'] == 1997


def test_check_duplicate_user_data(client, init_database, user_setup):
    test_user1, test_user2 = user_setup
    # with pytest.raises(IntegrityError):
    with pytest.raises(UserAlreadyExists):
        create_user(user_name=test_user1.user_name, user_email=test_user1.user_email,
                    password=test_user1.password, year_of_birth=test_user1.year_of_birth)


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

# ________________________________________________________________________________________________________________

