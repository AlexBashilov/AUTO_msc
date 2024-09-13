from http import HTTPStatus

import pytest

from api.api_client import ApiClient
from api.utils import assert_schema
from api.vehicle_api import get_vehicle
from api.models.getVehicle_models import GetVehicleResponseSchema, GetVehicleErrorSchema


class TestGetVehicle:
    """
    Тесты /getVehicle
    """

    @pytest.fixture(scope='class')
    def client(self):
        return ApiClient()

    def test_get_vehicle(self, client):
        """
        Получение ТС по id
        """
        body = {"params": {"id": 934}, "requestId": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5"}
        response = get_vehicle(client, body)
        assert response.status_code == HTTPStatus.OK, f"Код ответа {response.status_code}"
        assert_schema(response, GetVehicleResponseSchema)

    def test_get_vehicle_send_not_exist_vehicle(self, client):
        """
        Получить не существующее транспортное средство
        """
        body = {"params": {"id": 999999}, "requestId": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5"}
        response = get_vehicle(client, body)

        assert response.status_code == HTTPStatus.BAD_REQUEST, f"Код ответа {response.status_code}"
        assert_schema(response, GetVehicleErrorSchema)
        response_json = GetVehicleErrorSchema.model_validate_json(response.content)
        assert (
                response_json.errors[0].message == "Ошибка обработки получения ТС: Транспорт с таким ID не существует"
        ), "Текст ошибки отличается от ожидаемого"
