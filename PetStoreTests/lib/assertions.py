import json

from requests import Response


class Assertions:
    @staticmethod
    def assert_status_code(response: Response, expected_code, error_message):
        assert response.status_code == expected_code, error_message

    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in json format, Response text is {response.text}"

        assert name in response_as_dict, f"response JSON doesnt have key{name}"
        assert response_as_dict[name] == expected_value[name], error_message

    @staticmethod
    def assert_not_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in json format, Response text is {response.text}"

        assert name in response_as_dict, f"response JSON doesnt have key{name}"
        assert response_as_dict[name] != expected_value[name], error_message
