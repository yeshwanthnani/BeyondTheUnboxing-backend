from models.model import db, Mobile
from app import app
import json
import pytest
from tests.create_mobile import create_mobile
from models.exceptions import MobileAlreadyExists

@pytest.fixture

def client():
    with app.test_client() as client:
        yield client
@pytest.fixture()
def init_database(request):
    with app.app_context():
        def teardown():
            with app.app_context():
                db.session.query(Mobile).filter(Mobile.mobile_name.in_(['test_mobile_name1', 'test_mobile_name2', 'NewMobileName'])).delete()
                db.session.commit()

            # Add the teardown function as a finalizer
        request.addfinalizer(teardown)
        yield db
        # Commit the changes
        db.session.commit()

@pytest.fixture()
def mobile_data_setup():
    test_mobile_1 = create_mobile(brand="TestBrand1", mobile_name="test_mobile_name1")
    test_mobile_2 = create_mobile(brand="TestBrand2", mobile_name="test_mobile_name2")
    return test_mobile_1, test_mobile_2


def test_create_mobile(client, init_database):
    # Data for creating a new user
    new_mobile_data = {
        'brand': 'NewMobileBrand',
        'mobile_name': 'NewMobileName',
    }
    response = client.post('/api/v1/mobile/', data=json.dumps(new_mobile_data), content_type='application/json')
    # Check if the response is successful
    assert response.status_code == 201
    assert 'mobile_ID' in response.json
    assert response.json['message'] == 'New mobile entry created successfully'
    new_mobile_created = Mobile.query.filter_by(mobile_name='NewMobileName').first()
    assert new_mobile_created is not None
    assert new_mobile_created.brand == "NewMobileBrand"



def test_get_mobile_details1_by_mobile_ID(client, init_database, mobile_data_setup):
    test_mobile_1, test_mobile_2 = mobile_data_setup

    response = client.get(f'/api/v1/mobile/{test_mobile_1.mobile_ID}')
    assert response.status_code == 200
    assert response.json["brand"] == "TestBrand1"
    assert response.json["mobile_name"] == "test_mobile_name1"


def test_get_mobile_details2_by_mobile_ID(client, init_database, mobile_data_setup):
    test_mobile_1, test_mobile_2 = mobile_data_setup

    response = client.get(f'/api/v1/mobile/{test_mobile_2.mobile_ID}')
    assert response.status_code == 200
    assert response.json["brand"] == "TestBrand2"
    assert response.json["mobile_name"] == "test_mobile_name2"



def test_check_duplicate_mobile_data(client, init_database, mobile_data_setup):
    test_mobile_1, test_mobile_2 = mobile_data_setup

    with pytest.raises(MobileAlreadyExists):
        create_mobile(brand=test_mobile_1.brand, mobile_name=test_mobile_1.mobile_name)


def test_get_all_mobile_entries(client, init_database):
    response = client.get('api/v1/mobile/all/')
    assert response.status_code == 200

