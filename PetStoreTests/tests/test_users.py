from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.config import Payloads
import allure


class TestUser:

    def test_login_user(self):
        user_name ="testuser"
        password = "testpassword"

        login_user_response = MyRequests.get(f"/user/login?username={user_name}&password={password}")
        Assertions.assert_status_code(login_user_response, 200)

    def test_can_create_user(self):
        pass


    def test_can_update_user(self):
        pass

    def test_can_delete_user(self):
        pass

    def test_can_create_list_of_users(self):
        pass
