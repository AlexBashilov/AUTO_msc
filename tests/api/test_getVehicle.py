import uuid
from http import HTTPStatus

import allure

from api_utils.utils import assert_schema, assert_response_code, assert_error_message
from api_utils.vehicle_api import get_vehicle
from api_utils.models.getVehicle_models import GetVehicleResponseSchema, GetVehicleErrorSchema, GetVehicleRequestSchema, \
    VehicleRequestParams


class TestGetVehicle:
    @allure.id(38875)
    @allure.title('Получение ТС по id')
    def test_get_vehicle(self, client):
        body = GetVehicleRequestSchema(
            requestId=str(uuid.uuid4()),
            params=VehicleRequestParams(id=934)
        )
        response = get_vehicle(client, body)
        assert_response_code(HTTPStatus.OK, response.status_code)
        assert_schema(response, GetVehicleResponseSchema)

    @allure.id(37053)
    @allure.title('Получить не существующее транспортное средство')
    def test_get_vehicle_send_not_exist_vehicle(self, client):
        body = GetVehicleRequestSchema(
            requestId=str(uuid.uuid4()),
            params=VehicleRequestParams(id=999999)
        )
        response = get_vehicle(client, body)
        assert_response_code(HTTPStatus.BAD_REQUEST, response.status_code)
        assert_schema(response, GetVehicleErrorSchema)
        response_json = GetVehicleErrorSchema.model_validate_json(response.content)
        assert_error_message("Ошибка обработки получения ТС: Транспорт с таким ID не существует",
                             response_json.errors[0].message)
