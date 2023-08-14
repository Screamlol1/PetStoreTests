import random
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.config import Payloads
import allure
import json





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



@allure.epic("Order creation test")
class TestStore:
    endpoint = "/store/order"

    @allure.description("This is failed attempt to get no existed order ")
    def test_can_not_get_non_existent_order(self):
        not_found_response_text = {
            "code": 404,
            "type": "unknown",
            "message": "Order Not Found"
        }

        payload = Payloads.new_payload("ORDER", Payloads.id_generator())
        # create new order
        create_order_response = MyRequests.post("/store/order", data=payload)
        Assertions.assert_status_code(create_order_response, 200, "wrong code expected result 200")
        # check order exists
        create_order_data = create_order_response.json()
        order_id = create_order_data["id"]
        get_order_response = MyRequests.get(f"/store/order/{order_id}")
        Assertions.assert_status_code(get_order_response, 200, "wrong code expected result 200")
        #  delete order
        delete_order_response = MyRequests.delete(f"/store/order/{order_id}")
        Assertions.assert_status_code(delete_order_response, 200, "wrong code expected result 200")
        #  check order not exists anymore
        get_order_response = MyRequests.get(f"/store/order/{order_id}")
        Assertions.assert_status_code(get_order_response, 404, "wrong code expected result 200")
        # Assertions.assert_json_value_by_name(get_order_response, "message", not_found_response_text, "Wrong message")

    @allure.description("This is successfully order creation")
    def test_can_create_order(self):
        payload = Payloads.new_payload("ORDER", Payloads.id_generator())
        #  create new order and check it's created
        create_order_response = MyRequests.post("/store/order", data=payload)
        Assertions.assert_status_code(create_order_response, 200, "wrong code expected result 200")
        create_order_data = create_order_response.json()
        order_id = create_order_data["id"]
        #  check order exists and valid
        get_order_response = MyRequests.get(f"/store/order/{order_id}")
        Assertions.assert_status_code(get_order_response, 200, "wrong code expected result 200")
        Assertions.assert_json_value_by_name(get_order_response, "id", payload, "id are not equal")


    def test_can_update_order(self):
        pass

    def test_can_delete_order(self):
        pass




class TestUser:
    endpoint = "https://petstore.swagger.io/v2/pet"

    def test_can_get_user(self):
        pass

    def test_can_create_user(self):
        pass

    def test_can_update_user(self):
        pass

    def test_can_delete_user(self):
        pass

    def test_can_create_list_of_users(self):
        pass

