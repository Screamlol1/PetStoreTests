from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name}"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find header with name {header_name}"
        return response.headers[header_name]


class Payloads:
    def new_payload(self, case, some_id):
        if case == "PET":
            return {
                "id": some_id,
                "category": {
                    "id": 1,
                    "name": "string"
                },
                "name": "testdoggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 1,
                        "name": "string"
                    }
                ],
                "status": "available"
            }
        elif case == "ORDER":
            return {
                "id": 1,
                "petId": 1,
                "quantity": 0,
                "shipDate": "2023-08-10T22:43:07.630Z",
                "status": "placed",
                "complete": true
            }
        elif case == "USER":
            return {
                "id": 9776753495,
                "username": "string1",
                "firstName": "string",
                "lastName": "string",
                "email": "123",
                "password": "string",
                "phone": "string",
                "userStatus": 1
            }
        elif case == "LIST":