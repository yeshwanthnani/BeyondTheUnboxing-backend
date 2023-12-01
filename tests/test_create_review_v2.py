import pytest
from models.model import UserAccount,Mobile,db
from controllers import  review_controller



@pytest.fixture
def create_user_and_mobile():
    user_1 = UserAccount(
        user_name="mohan",
        user_email="mohan145krishna@gmail.com",
        password="qwerty123",
        year_of_birth=1998
    )

    mobile_1 =  Mobile(
            brand = "Samsung",
            mobile_name = "GALAXY NOTE 10"
        )

    db.session.add(user_1)
    db.session.add(mobile_1)

    db.session.commit()

    return  user_1.user_ID , mobile_1.mobile_ID


def test_create_user_review_for_a_mobile(create_user_and_mobile):
    user_id, mobile_id = create_user_and_mobile

    review_controller.create_review()
