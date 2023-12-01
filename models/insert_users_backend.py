import json

import requests


basr_url = "http://127.0.0.1:5000/api/v1"

def test_create_user_successful_case():

    endpoint = basr_url +"/user/"

    body = {
        "user_name":"mohan krishna",
        "user_email":"mohan145krishna@gmail.com",
        "password":"qwerty123",
        "year_of_birth":1998
    }
    body = json.dumps(body)
    headers = {
        "Content-Type":"application/json"
    }
    response = requests.post(url=endpoint, data=body, headers=headers)
    assert  response.status_code == 201
    print(response)


if __name__ == '__main__':
    test_create_user_successful_case()

