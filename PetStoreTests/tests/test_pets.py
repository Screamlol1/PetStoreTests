from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.config import Payloads
import allure


@allure.epic("Pet creation cases")
class TestPets:

    @allure.description("This is successfully pet creating")
    def test_can_create_pet(self):
        #  create test data for new pet
        payload = Payloads.new_payload("PET", Payloads.id_generator())
        # create new pet
        create_pet_response = MyRequests.post("/pet", data=payload)
        # check successfully created
        Assertions.assert_status_code(create_pet_response, 200, "wrong code expected result 200")
        # get pet by id and check it's successfully
        create_pet_data = create_pet_response.json()
        pet_id = create_pet_data["id"]
        get_pet_response = MyRequests.get(f"/pet/{pet_id}")
        Assertions.assert_status_code(get_pet_response, 200, "wrong code expected result 200")
        Assertions.assert_json_value_by_name(get_pet_response, "name", payload, "name's are not equal")
        Assertions.assert_json_value_by_name(get_pet_response, "id", payload, "id's are not equal")

    @allure.description("This is successfully update pet data")
    def test_can_update_pet(self):
        payload = Payloads.new_payload("PET", Payloads.id_generator())
        create_pet_response = MyRequests.post("/pet", data=payload)
        Assertions.assert_status_code(create_pet_response, 200, "wrong code expected result 200")
        pet_id = create_pet_response.json()["id"]

        new_payload = Payloads.new_payload("UPDATED PET", pet_id)
        update_pet_response = MyRequests.put("/pet", data=new_payload)
        Assertions.assert_status_code(update_pet_response, 200, "wrong code expected result 200")

        #       get pet and validate the changes
        get_pet_response = MyRequests.get(f"/pet/{pet_id}")
        Assertions.assert_status_code(get_pet_response, 200, "wrong code expected result 200")
        Assertions.assert_json_value_by_name(get_pet_response, "name", new_payload, "names are not equal")
        Assertions.assert_json_value_by_name(get_pet_response, "status", new_payload, "status is not the same")
        Assertions.assert_not_json_value_by_name(get_pet_response, "name", payload, "names are  equal")
        Assertions.assert_not_json_value_by_name(get_pet_response, "status", payload, "status is  the same")

    @allure.description("This is successfully pet remove")
    def test_can_delete_oet(self):
        #       add the pet
        payload = Payloads.new_payload("PET", Payloads.id_generator())
        create_pet_response = MyRequests.post("/pet", data=payload)
        Assertions.assert_status_code(create_pet_response, 200, "wrong code expected result 200")
        pet_id = create_pet_response.json()["id"]
        get_pet_response = MyRequests.get(f"/pet/{pet_id}")
        Assertions.assert_status_code(get_pet_response, 200, "wrong code expected result 200")
        #       delete the pet
        delete_pet_response = MyRequests.delete(f"/pet/{pet_id}")
        Assertions.assert_status_code(delete_pet_response, 200, "wrong code expected result 200")
        #       get the pet and check that it's not found
        get_pet_response = MyRequests.get(f"/pet/{pet_id}")
        Assertions.assert_status_code(get_pet_response, 404, "wrong code expected result 404")
