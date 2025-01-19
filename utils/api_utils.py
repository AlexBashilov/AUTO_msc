from typing import Type


import os


from pydantic import BaseModel
from httpx import Client, Response


class ApiClient(Client):
    """
    Расширение стандартного клиента httpx.
    """

    def __init__(self):
        super().__init__(
            base_url=os.getenv("SANDBOX")
        )



def assert_schema(response, model: Type[BaseModel]) -> BaseModel:
    body = response.json()
    if isinstance(body, list):
        for item in body:
            model.model_validate(item, strict=True)
    else:
        model.model_validate(body, strict=True)

    return model.model_validate(response.json())



def assert_response_code(expected_code, actual_code):
    assert actual_code == expected_code, f"Код ответа {actual_code}"



def assert_error_message(expected_error, actual_error):
    assert actual_error == expected_error, "Текст ошибки отличается от ожидаемого"



def post_request(client, body: BaseModel, route) -> Response:

    response = client.post(route, json=body.model_dump())
    return response

def get_request(client, route) -> Response:
    response = client.get(route)
    return response



def assert_response_data(expected_response: BaseModel, response):
    diff = _compare_json(
        expected_response.model_dump(exclude_none=True), response.json()
    )
    assert not diff, f"Данные в ответе отличаются от ожидаемых - {diff}"



def _compare_json(expected_json, actual_json, path="") -> list[str]:
    differences = []

    if isinstance(expected_json, dict) and isinstance(actual_json, dict):
        all_keys = set(expected_json.keys()).union(set(actual_json.keys()))

        for key in all_keys:
            full_path = f"{path}.{key}" if path else key

            if key not in expected_json:
                differences.append(f"Ключ '{full_path}' отсутствует в expected_json")
            elif key not in actual_json:
                differences.append(f"Ключ '{full_path}' отсутствует в actual_json")
            else:
                differences.extend(
                    _compare_json(expected_json[key], actual_json[key], full_path)
                )

    elif isinstance(expected_json, list) and isinstance(actual_json, list):
        min_len = min(len(expected_json), len(actual_json))
        for index in range(min_len):
            full_path = f"{path}[{index}]"
            differences.extend(
                _compare_json(expected_json[index], actual_json[index], full_path)
            )

        if len(expected_json) > len(actual_json):
            for index in range(min_len, len(expected_json)):
                differences.append(
                    f"В актуальном ответе не хватает объекта '{path}[{index}]': {expected_json[index]}"
                )
        elif len(actual_json) > len(expected_json):
            for index in range(min_len, len(actual_json)):
                differences.append(
                    f"В актуальном ответе лишний объект '{path}[{index}]': {actual_json[index]}"
                )

    elif expected_json != actual_json:
        differences.append(
            f"Значение в '{path}' отличаются: ожидаемое - {expected_json} | актуальное - {actual_json}"
        )

    return differences
