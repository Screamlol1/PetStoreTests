# Проект PetStoreTests

## Используемые технологии
Python,
Pytest,
requests,
Allure,
Docker

## Описание проекта:

Pet-проект реализации автотестирования Rest Api.

 В качестве объекта тестирования выбран сайт https://petstore.swagger.io/ с открытым api.

Сайт позволяет получать информацию о питомцах, заказах и пользователях, а также создавать их.

## Список проверок, реализованных в автотестах:

test_can_create_order - создать новый заказ

test_can_delete_order - удалить заказ

test_delete_non_existent_order удалить не существующий заказ

test_can_get_inventory получить инвентарь

test_can_create_pet создать новое животное

test_can_update_pet обновить данные о животном

test_can_delete_oet удалить животное

test_login_user авторизовать юзера по логину и паролю

test_logout_user разлогинить юзера

test_can_update_user обновить данные юзера

test_can_delete_user удалить юзера

test_can_create_list_of_users создать список юзеров



## Пример запуска из командной строки:

python -m pytest  -v -s

### Запуск автотестов в контейнере docker

docker build -t pytest_runner

docker run --rm --mount type=bind,src="project_dir"\PetStoreTests,target=/tests_project/ pytest_runner

