import uuid
from http import HTTPStatus
import allure
from api_utils.utils import assert_schema, assert_response_code, assert_error_message
from api_utils import utils
from api_utils import routes
from api_utils.models.getDriver_models import GetDriverResponseSchema, GetDriverErrorSchema, GetDriverRequestSchema, \
    DriverRequestParams
from data_base.models.drivers_db import DriversDB
from data_base.db_queries import SqlQueries


class TestGetDriver:
    @allure.id(57839)
    @allure.title('Получение водителя по id')
    def test_get_driver(self, client, db_connection):
        db = SqlQueries(db_connection)
        new_driver = DriversDB.generate_random_driver()
        db.insert_new_driver(new_driver)
        body = GetDriverRequestSchema(
            requestId=str(uuid.uuid4()),
            params=DriverRequestParams(id=4531)
        )
        response = utils.post_request(client, body, routes.Routes.GET_DRIVER)
        assert_response_code(HTTPStatus.OK, response.status_code)
        assert_schema(response, GetDriverResponseSchema)

    @allure.id(37467)
    @allure.title('Получить не существующего водителя')
    def test_get_driver_send_not_exist_driver(self, client):
        body = GetDriverRequestSchema(
            requestId=str(uuid.uuid4()),
            params=DriverRequestParams(id=999999)
        )
        response = utils.post_request(client, body, routes.Routes.GET_DRIVER)
        assert_response_code(HTTPStatus.BAD_REQUEST, response.status_code)
        assert_schema(response, GetDriverErrorSchema)
        response_json = GetDriverErrorSchema.model_validate_json(response.content)
        assert_error_message("Ошибка обработки получения ТС: Транспорт с таким ID не существует",
                             response_json.errors[0].message)
