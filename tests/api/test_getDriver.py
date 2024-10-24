import uuid
from http import HTTPStatus
import allure
import utils.api_utils as api_utils
from api_pages import routes
from api_pages.models import getDriver as driver_models
from data_base.models.drivers_db import DriversDB
from data_base.db_queries import SqlQueries


class TestGetDriver:
    @allure.id(57839)
    @allure.title('Получение водителя по id')
    def test_get_driver(self, client, db_connection):
        db = SqlQueries(db_connection)
        new_driver = DriversDB.generate_random_driver()
        driver_id = db.insert_new_driver(new_driver)
        body = driver_models.GetDriverRequestSchema(
            requestId=str(uuid.uuid4()),
            params=driver_models.DriverRequestParams(id=driver_id)
        )
        response = api_utils.post_request(client, body, routes.Routes.GET_DRIVER)
        api_utils.assert_response_code(HTTPStatus.OK, response.status_code)
        api_utils.assert_schema(response, driver_models.GetDriverResponseSchema)
        db.delete_driver_by_id(driver_id)
