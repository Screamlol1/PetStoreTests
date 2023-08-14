import random


class Payloads:
    @staticmethod
    def id_generator():
        return random.randint(100000, 999999)

    @staticmethod
    def new_payload(case, some_id):
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
                "id": some_id,
                "petId": 1,
                "quantity": 0,
                "shipDate": "2023-08-10T22:43:07.630Z",
                "status": "placed",
                "complete": "true"
            }
        elif case == "USER":
            return {
                "id": some_id,
                "username": "string1",
                "firstName": "string",
                "lastName": "string",
                "email": "123",
                "password": "string",
                "phone": "string",
                "userStatus": 1
            }
        elif case == "EMPTY":
            return {}
        elif case == "UPDATED PET":
            return {
                "id": some_id,
                "category": {
                    "id": 1,
                    "name": "string"
                },
                "name": "updatedtestdoggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 1,
                        "name": "string"
                    }
                ],
                "status": "sold"
            }



