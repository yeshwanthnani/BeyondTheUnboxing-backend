# test_user_cases.py

import pytest
from models.create_user import create_user
from models.model import db, UserAccount
from app import app

@pytest.fixture

def user_setup():
    test_user1 = create_user(user_name="kranthi", user_email="Kranthi@gmail.com", password="HJKLIJ@90", year_of_birth=1997)
    test_user2 = create_user(user_name="yesh", user_email="Yesh@gmail.com", password="7545fdygJ@90", year_of_birth=1997)

    assert test_user1 is not None
    assert test_user2 is not None

    yield test_user1, test_user2  # Return the created UserAccount instances as a tuple

    # db.session.delete(test_user1)
    # db.session.delete(test_user2)
    db.session.commit()

def test_user_creation(user_setup):
    test_user1, test_user2 = user_setup

    # Check if the user data is loaded correctly
    assert test_user1.user_name == "kranthi"
    assert test_user2.user_name == "yesh"
    # Add more assertions to check other attributes as needed
