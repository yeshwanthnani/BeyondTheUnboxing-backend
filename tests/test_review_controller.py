from models.model import db ,Mobile ,Question,UserAccount, Review
from app import app
import json
import pytest
from tests.create_reviews import create_user_review
from tests.create_user import create_user
from tests.create_mobile import create_mobile

@pytest.fixture

def client():
    with app.test_client() as client:
        yield client

@pytest.fixture()
def init_database(request):
    with app.app_context():
        def teardown():
            with app.app_context():
                user_ids = [user.user_ID for user in UserAccount.query.filter(UserAccount.user_name == 'test_uname_review')]
                mobile_ids = [mobile.mobile_ID for mobile in
                              Mobile.query.filter(Mobile.mobile_name == 'test_mname_review')]

                # Delete records from Review table
                db.session.query(Review).filter(Review.user_ID.in_(user_ids), Review.mobile_ID.in_(mobile_ids)).delete()

                # Delete records from UserAccount table
                db.session.query(UserAccount).filter(UserAccount.user_ID.in_(user_ids)).delete()

                # Delete records from Mobile table
                db.session.query(Mobile).filter(Mobile.mobile_ID.in_(mobile_ids)).delete()

                db.session.commit()

                # Add the teardown function as a finalizer
            request.addfinalizer(teardown)
            yield db
            # Commit the changes
            db.session.commit()


@pytest.fixture()
def review_data_setup():
    test_user_1 = create_user(user_name="test_uname_review", user_email="testreview@gmail.com", password="HJKLIJ@90",
                             year_of_birth=1997)
    test_mobile_1 = create_mobile(brand="TestBrand_review", mobile_name="test_mname_review")

    rating_data = [1,2,4,5,3,4,5,3,4,1]

    return test_user_1, test_mobile_1, rating_data

def test_adding_reviews_for_test_user(client,init_database, review_data_setup):
    test_user_1, test_mobile_1,rating_data = review_data_setup

    user_response = client.get(f'/api/v1/user/{test_user_1.user_ID}')
    assert user_response.status_code == 200
    existing_user_id = test_user_1.user_ID
    mobile_response = client.get(f'/api/v1/mobile/{test_mobile_1.mobile_ID}')
    assert mobile_response.status_code == 200
    existing_mobile_id = test_mobile_1.mobile_ID

    create_user_review(existing_user_id, existing_mobile_id, rating_data)







