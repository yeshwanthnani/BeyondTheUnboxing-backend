from models.model import db
from app import app
from models.model import Mobile
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
        Mobile.query.delete()

        # Commit the changes
        db.session.commit()


def test_get_mobile(client, init_database):
    test_mobile = Mobile(brand ="Test brand", mobile_name="Test mobile name")
    init_database.session.add(test_mobile)
    init_database.session.commit()

    # Send a GET request to retrieve the user
    response = client.get(f'/api/v1/mobile/{test_mobile.mobile_ID}')

    #check if response is correct
    assert response.status_code == 200

    # Check if the returned data matches the test user's data
    assert response.json['brand'] == "Test brand"
    assert response.json["mobile_name"] == "Test mobile name"

def test_create_mobile(client, init_database):

    test_mobile_data={
        "brand": "Test brand",
        "mobile_name": "Test mobile name"
    }

    #send a POST response to create a new entry in the mobile table
    response = client.post('/api/v1/mobile/', data= json.dumps(test_mobile_data), content_type= "application/json")


    assert response.status_code == 201

    # Check if the returned data contains the mobile_ID and message
    assert 'mobile_ID' in response.json
    assert response.json['message'] == 'New mobile entry created successfully'


    #check if the mobile is added to the data base
    new_mobile = Mobile.query.filter_by(brand='Test brand').first()

    assert new_mobile is not None
    assert new_mobile.brand == "Test brand"
    assert new_mobile.mobile_name == "Test mobile name"




