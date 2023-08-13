import requests
endpoint = "https://petstore.swagger.io/v2/pet"
class TestPets:
    def test_get_pet_by_id(self):
        url = "https://petstore.swagger.io/v2/pet/"
        pet_id = '9776753499'
        data = {'petid': pet_id}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "wrong code"

        #
        # response_dict = response.json()
        # assert "answer" in response_dict, "there is no such field"


# response = requests.get("https://petstore.swagger.io/v2/pet/9223372036854309000")
# print(response.status_code)