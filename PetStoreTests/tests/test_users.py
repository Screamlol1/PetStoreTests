from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.config import Payloads
import allure

@allure.epic("Operations with users")
class TestUser:
    @allure.description("This is successfully login test")
    def test_login_user(self):
        user_name ="testuser"
        password = "testpassword"

        login_user_response = MyRequests.get(f"/user/login?username={user_name}&password={password}")
        Assertions.assert_status_code(login_user_response, 200)
    @allure.description("This is successfully logout test")
    def test_logout_user(self):
        logout_user_response = MyRequests.get("/user/logout")
        Assertions.assert_status_code(logout_user_response, 200)
        Assertions.assert_json_value_by_name(logout_user_response, "message", "ok", "wrong message")


    def test_can_create_list_of_users(self):
        pass

    def test_can_delete_user(self):
        pass

    def test_can_create_list_of_users(self):
        pass
