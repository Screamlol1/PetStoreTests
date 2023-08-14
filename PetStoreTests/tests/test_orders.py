from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.config import Payloads
import allure


@allure.epic("Order creation test")
class TestStore:
    endpoint = "/store/order"

    @allure.description("This is failed attempt to get no existed order ")
    def test_can_not_get_non_existent_order(self):
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