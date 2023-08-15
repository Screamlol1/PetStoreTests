import json

from requests import Response


class Assertions:
    @staticmethod
    def assert_status_code(response: Response, expected_code):
        assert response.status_code == expected_code, f"Unexpected status code Expected: {expected_code} , Actual: {response.status_code}"

    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in json format, Response text is {response.text}"

        assert name in response_as_dict, f"response JSON doesnt have key{name}"
        assert response_as_dict[name] == expected_value, error_message


    @staticmethod
    def assert_json_value_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in json format, Response text is {response.text}"

        assert name in response_as_dict, f"response JSON doesnt have key{name}"

    @staticmethod
    def assert_json_value_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in json format, Response text is {response.text}"

        assert name not in response_as_dict, f"response JSON doesnt have key{name}"



