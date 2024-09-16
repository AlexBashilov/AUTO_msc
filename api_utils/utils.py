from typing import Type

import allure
from pydantic import BaseModel


@allure.step("Проверить что ответ соответствует схеме")
def assert_schema(response, model: Type[BaseModel]):
    """
    Проверяет тело ответа на соответствие его схеме механизмами pydantic
    :param response: ответ от сервера
    :param model: модель, по которой будет проверяться схема json
    :raises ValidationError: если тело ответа не соответствует схеме
    """
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
