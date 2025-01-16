from http import HTTPStatus
import allure
import pytest
from faker import Faker
from allure import title, id
import utils.api_utils as api_utils
from api_pages import routes
from api_pages.models import createDriver
from api_pages.models.createDriver import (
    CreateDriverErrorSchema,
    ErrorMessage,
    ErrorData,
)
from data_base.db_queries import SqlQueries
import pages.api.data_validation as data_validation
from test_data.api.error_create_driver import CreateDriverError
from test_data.api.test_params.create_driver import (
    create_valid_drivers_parameters,
    create_drivers_required_parameters,
    create_drivers_errors,
)


class TestCreateDriver:
    @pytest.mark.parametrize("test_param", create_valid_drivers_parameters())
    def test_create_valid_driver(self, client, db_connection, test_param):
        db = SqlQueries(db_connection)
        allure.dynamic.title(test_param["name"])
        allure.dynamic.id(test_param["allureID"])
        response = api_utils.post_request(client, test_param["request_body"], routes.Routes.CREATE_DRIVER)
        api_utils.assert_response_code(HTTPStatus.OK, response.status_code)
        response_model = api_utils.assert_schema(response, createDriver.CreateDriverResponseSchema)
        driver_data = db.get_driver_by_id(response_model.result.id)
        driver_tc = db.get_tc_by_driver_id(response_model.result.id)
        data_validation.create_driver_validation_data(test_param["request_body"], driver_data, driver_tc)
        db.delete_driver_by_id(response_model.result.id)

    @pytest.mark.parametrize("test_param", create_drivers_required_parameters())
    def test_create_driver_required_params(self, client, test_param):
        allure.dynamic.title(test_param["name"])
        allure.dynamic.id(test_param["allureID"])
        response = api_utils.post_request(client, test_param["request_body"], routes.Routes.CREATE_DRIVER)
        api_utils.assert_response_code(HTTPStatus.UNPROCESSABLE_ENTITY, response.status_code)
        response_model = api_utils.assert_schema(response, createDriver.CreateDriverRequiredParamsErrorSchema)
        api_utils.assert_error_message(test_param["expected_error"], response_model.message)

    @pytest.mark.parametrize("test_param", create_drivers_errors())
    def test_create_driver_error(self, client, test_param):
        allure.dynamic.title(test_param["name"])
        allure.dynamic.id(test_param["allureID"])
        response = api_utils.post_request(client, test_param["request_body"], routes.Routes.CREATE_DRIVER)
        api_utils.assert_response_code(HTTPStatus.BAD_REQUEST, response.status_code)
        response_model = api_utils.assert_schema(response, createDriver.CreateDriverErrorSchema)
        api_utils.assert_error_message(test_param["expected_error"], response_model.errors[0].message)

    @title("Создания водителя с тем же номером паспорта")
    @id("37463")
    def test_create_driver_with_same_passport(self, client, db_connection):
        db = SqlQueries(db_connection)
        fake = Faker("ru_RU")
        driver = createDriver.CreateDriverRequestSchema(
            params=createDriver.CreateDriverRequestParams(
                transportCompanyIds=[39],
                surname=fake.last_name(),
                name=fake.first_name(),
                patronymic=fake.middle_name(),
                phoneNumber=fake.bothify("9#########"),
                passportFullNumber=fake.passport_number(),
                passportDate=fake.date(),
                licenseNumber=str(fake.random_number(digits=10)),
            )
        )
        valid_response = api_utils.post_request(client, driver, routes.Routes.CREATE_DRIVER)
        api_utils.assert_response_code(HTTPStatus.OK, valid_response.status_code)
        valid_response_model = api_utils.assert_schema(valid_response, createDriver.CreateDriverResponseSchema)
        driver_data = db.get_driver_by_id(valid_response_model.result.id)
        driver_tc = db.get_tc_by_driver_id(valid_response_model.result.id)
        data_validation.create_driver_validation_data(driver, driver_data, driver_tc)
        expected_error_response = CreateDriverErrorSchema(
            errors=[
                ErrorMessage(
                    data=ErrorData(anotherDriverId=valid_response_model.result.id),
                    message=CreateDriverError.SAME_PASSPORT_ERROR,
                )
            ]
        )
        error_response = api_utils.post_request(client, driver, routes.Routes.CREATE_DRIVER)
        api_utils.assert_response_code(HTTPStatus.BAD_REQUEST, error_response.status_code)
        api_utils.assert_schema(error_response, createDriver.CreateDriverErrorSchema)
        api_utils.assert_response_data(expected_error_response, error_response)
        db.delete_driver_by_id(valid_response_model.result.id)
