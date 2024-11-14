from typing import Type

import allure
import os
from allure_commons.types import AttachmentType
from pydantic import BaseModel
from httpx import Client, Response


class ApiClient(Client):
    """
    Расширение стандартного клиента httpx.
    """

    def __init__(self):
        super().__init__(base_url='https://tms-api-rest.intgr-test-' + os.getenv('STAGE') + '.ox1.dev/api')


@allure.step("Проверить что ответ соответствует схеме")
def assert_schema(response, model: Type[BaseModel]):
    body = response.json()
    if isinstance(body, list):
        for item in body:
            model.model_validate(item, strict=True)
    else:
        model.model_validate(body, strict=True)


@allure.step("Проверить код ответа")
def assert_response_code(expected_code, actual_code):
    assert actual_code == expected_code, f"Код ответа {actual_code}"


@allure.step("Проверить текст ошибки")
def assert_error_message(expected_error, actual_error):
    assert (
            actual_error == expected_error
    ), "Текст ошибки отличается от ожидаемого"


@allure.step("Отправить POST запрос на ручку {1}")
def post_request(client, body: BaseModel, route) -> Response:
    response = client.post(route, json=body.dict())
    allure.attach(response.content, name="Ответ", attachment_type=AttachmentType.JSON)
    return response
