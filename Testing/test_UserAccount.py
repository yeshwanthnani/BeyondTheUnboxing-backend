# test_data_setup.py


import pytest

from models.Constants import HttpStatus, ResponseMessages
from models.model import db
import json
from app import app
from models.model import UserAccount
from controllers.user_controller import create_user, delete_user, get_user
from flask import Response
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
                try:
                    db.session.rollback()
                except Exception as e:
                    print(f"Error during rollback: {e}")
                finally:
                    db.session.close()
            # Add the teardown function as a finalizer
        request.addfinalizer(teardown)
        yield db
        # Commit the changes
        db.session.commit()


@pytest.fixture()
def single_user_setup(request):
    new_user1 = UserAccount(
        user_name="kranthi",
        user_email="unique_email_for_test@gmail.com",
        password="asdfgh@90",
        year_of_birth=1997
    )

    def teardown():
        db.session.delete(new_user1)
        db.session.commit()

    request.addfinalizer(teardown)
    return new_user1


def test_create_user_user_does_not_exist(client, init_database, single_user_setup):

    existing_user = single_user_setup
    response = create_user("Mohan","mohan145krishna@gmail.com","querty123",1998)
    assert response.status_code == HttpStatus.CREATED.value
    assert response.json['data']['user_name'] == 'Mohan'
    assert response.json['data']['user_email'] == 'mohan145krishna@gmail.com'
    assert response.json['data']['user_ID'] is not None


# def test_delete_user_user_exist(client, init_database, single_user_setup):
#     existing_user = single_user_setup
#     response = delete_user(user_email=existing_user.user_email)  # Pass the user's email
#     assert response.status_code == HttpStatus.SUCCESS.value
#     assert response.json['message'] == ResponseMessages.DELETED


# def test_get_user_details(client, init_database, single_user_setup):
#
#     res = get_user(140)
#     assert res.json['user_name'] == 'Mohan'
#     # assert res.json['user_email'] == 'yeshwanth@gmail.com'
