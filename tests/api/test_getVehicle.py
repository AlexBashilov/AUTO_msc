import uuid
from http import HTTPStatus
import utils.api_utils as api_utils
from api_pages import routes
from api_pages.models import getVehicle as vehicle_models
from data_base.models.vehicle_db import VehicleDB
from data_base.db_queries import SqlQueries


class TestGetVehicle:

    def test_get_vehicle(self, client, db_connection):
        db = SqlQueries(db_connection)
        new_vehicle = VehicleDB.generate_random_vehicle()
        vehicle_id = db.insert_new_vehicle(new_vehicle)
        body = vehicle_models.GetVehicleRequestSchema(
            requestId=str(uuid.uuid4()),
            params=vehicle_models.VehicleRequestParams(id=vehicle_id),
        )
        response = api_utils.post_request(client, body, routes.Routes.GET_VEHICLE)
        api_utils.assert_response_code(HTTPStatus.OK, response.status_code)
        api_utils.assert_schema(response, vehicle_models.GetVehicleResponseSchema)
        db.delete_vehicle_by_id(vehicle_id)


    def test_get_vehicle_send_not_exist_vehicle(self, client):
        body = vehicle_models.GetVehicleRequestSchema(
            requestId=str(uuid.uuid4()),
            params=vehicle_models.VehicleRequestParams(id=999999),
        )
        response = api_utils.post_request(client, body, routes.Routes.GET_VEHICLE)
        api_utils.assert_response_code(HTTPStatus.BAD_REQUEST, response.status_code)
        api_utils.assert_schema(response, vehicle_models.GetVehicleErrorSchema)
        response_json = vehicle_models.GetVehicleErrorSchema.model_validate_json(
            response.content
        )
        api_utils.assert_error_message(
            "Ошибка обработки получения ТС: Транспорт с таким ID не существует",
            response_json.errors[0].message,
        )
