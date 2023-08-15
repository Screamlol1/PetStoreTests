from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.config import Payloads
import allure


@allure.epic("Operations with orders")
class TestStore:

    @allure.description("This is successfully order creation")
    def test_can_create_order(self):
        payload = Payloads.new_payload("ORDER", Payloads.id_generator())
        #  create new order and check it's created
        create_order_response = MyRequests.post("/store/order", data=payload)
        Assertions.assert_status_code(create_order_response, 200)
        create_order_data = create_order_response.json()
        order_id = create_order_data["id"]
        #  check order exists and valid
        get_order_response = MyRequests.get(f"/store/order/{order_id}")
        Assertions.assert_status_code(get_order_response, 200)
        Assertions.assert_json_value_by_name(get_order_response, "id", create_order_response.json()["id"],
                                             "id are not equal")

    @allure.description("This is successfully order delete test")
    def test_can_delete_order(self):
        payload = Payloads.new_payload("ORDER", Payloads.id_generator())
        # create new order
        create_order_response = MyRequests.post("/store/order", data=payload)
        Assertions.assert_status_code(create_order_response, 200)
        # check order exists
        create_order_data = create_order_response.json()
        order_id = create_order_data["id"]
        get_order_response = MyRequests.get(f"/store/order/{order_id}")
        Assertions.assert_status_code(get_order_response, 200)
        #  delete order
        delete_order_response = MyRequests.delete(f"/store/order/{order_id}")
        Assertions.assert_status_code(delete_order_response, 200)
        #  check order not exists anymore
        get_order_response = MyRequests.get(f"/store/order/{order_id}")
        Assertions.assert_status_code(get_order_response, 404)
        Assertions.assert_json_value_has_key(get_order_response, "message")
        Assertions.assert_json_value_by_name(get_order_response,"message", "Order not found", "wrong text message")\

    @allure.description("This is successfully non-expistent order delete test")
    def test_delete_non_existent_order(self):
        payload = Payloads.new_payload("ORDER", Payloads.id_generator())
        # create new order
        create_order_response = MyRequests.post("/store/order", data=payload)
        Assertions.assert_status_code(create_order_response, 200)
        # check order exists
        create_order_data = create_order_response.json()
        order_id = create_order_data["id"]
        get_order_response = MyRequests.get(f"/store/order/{order_id}")
        Assertions.assert_status_code(get_order_response, 200)
        #  delete order
        delete_order_response = MyRequests.delete(f"/store/order/{order_id}")
        Assertions.assert_status_code(delete_order_response, 200)
        # try to delete again
        delete_order_response = MyRequests.delete(f"/store/order/{order_id}")
        Assertions.assert_status_code(delete_order_response, 404)

    @allure.description("This is successfully inventory test")
    def test_can_get_inventory(self):
        create_get_response = MyRequests.get("/store/inventory")
        Assertions.assert_status_code(create_get_response, 200)
        Assertions.assert_json_value_has_key(create_get_response, "sold")
        Assertions.assert_json_value_has_key(create_get_response, "available")
        Assertions.assert_json_value_has_key(create_get_response, "pending")

