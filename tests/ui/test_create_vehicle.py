import allure
import pytest

from pages.base_page import Base
from pages.login_page import Login
from pages.transport_companies_page import TransportCompaniesPage
from pages.vehicle_page import VehiclePage

from test_data.transport_companies import TransportCompanies
from test_data.test_params.invalid_vehicle import InvalidVehicle
from test_data.test_params.valid_vehicle import ValidVehicle


class TestCreateVehicle:
    valid_vehicle = ValidVehicle().list_of_vehicle_parameters()
    invalid_vehicle = InvalidVehicle().list_of_invalid_vehicle_parameters()

    @pytest.mark.parametrize("example", valid_vehicle)
    def test_create_valid_vehicle(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)
        vehicle = VehiclePage(driver)
        transport_company = TransportCompanies().generate_random_tc(example["name"])

        allure.dynamic.title(
            "Создание транспортного средства с типом ТС " + example["name"]
        )
        allure.dynamic.id(example["allureID"])
        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_transport_companies_page()
        tc.create_transport_company()
        tc.fill_transport_company(transport_company)
        tc.save_transport_company()
        tc.filter_transport_company(transport_company)
        tc.go_to_first_transport_company_on_the_list()
        vehicle.create_vehicle()
        vehicle.fill_vehicle(example)
        vehicle.save_vehicle()
        vehicle.filter_vehicle(example)
        vehicle.delete_first_vehicle_on_the_list(example)
        vehicle.check_lack_vehicle_on_the_list(example)
        base.go_to_transport_companies_page()
        tc.filter_transport_company(transport_company)
        tc.delete_first_transport_company_on_the_list(transport_company)
        tc.check_lack_transport_company_on_the_list(transport_company)

    @pytest.mark.parametrize("example", invalid_vehicle)
    def test_create_invalid_vehicle(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)
        vehicle = VehiclePage(driver)
        transport_company = TransportCompanies().generate_random_tc(example["name"])

        allure.dynamic.title(example["name"])
        allure.dynamic.id(example["allureID"])
        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_transport_companies_page()
        tc.create_transport_company()
        tc.fill_transport_company(transport_company)
        tc.save_transport_company()
        tc.filter_transport_company(transport_company)
        tc.go_to_first_transport_company_on_the_list()
        vehicle.create_vehicle()
        vehicle.fill_vehicle(example)
        vehicle.check_error_message_after_save_vehicle(example["error"])
        base.close_info_modal()
        base.go_to_transport_companies_page()
        tc.filter_transport_company(transport_company)
        tc.delete_first_transport_company_on_the_list(transport_company)
        tc.check_lack_transport_company_on_the_list(transport_company)

    @pytest.mark.parametrize("example", valid_vehicle)
    def test_select_exist_vehicle(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)
        vehicle = VehiclePage(driver)
        transport_company_first = TransportCompanies().generate_random_tc(
            example["name"]
        )
        transport_company_second = TransportCompanies().generate_random_tc(
            example["name"]
        )

        allure.dynamic.title(
            "Добавление уже существующего ТС в ТК с типом ТС " + example["name"]
        )
        allure.dynamic.id(example["allureIdExistVehicle"])
        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_transport_companies_page()
        tc.create_transport_company()
        tc.fill_transport_company(transport_company_first)
        tc.save_transport_company()
        tc.filter_transport_company(transport_company_first)
        tc.go_to_first_transport_company_on_the_list()
        vehicle.create_vehicle()
        vehicle.fill_vehicle(example)
        vehicle.save_vehicle()
        base.go_to_transport_companies_page()
        tc.create_transport_company()
        tc.fill_transport_company(transport_company_second)
        tc.save_transport_company()
        tc.filter_transport_company(transport_company_second)
        tc.go_to_first_transport_company_on_the_list()
        vehicle.create_vehicle()
        vehicle.select_existing_vehicle(example)
        vehicle.save_vehicle()
        vehicle.click_on_vehicle_view()
        vehicle.check_note_existing_vehicle()
        base.go_to_transport_companies_page()
        tc.filter_transport_company(transport_company_second)
        tc.go_to_first_transport_company_on_the_list()
        vehicle.filter_vehicle(example)
        vehicle.delete_first_vehicle_on_the_list(example)
        vehicle.check_lack_vehicle_on_the_list(example)
        base.go_to_transport_companies_page()
        tc.filter_transport_company(transport_company_first)
        tc.go_to_first_transport_company_on_the_list()
        vehicle.filter_vehicle(example)
        vehicle.delete_first_vehicle_on_the_list(example)
        vehicle.check_lack_vehicle_on_the_list(example)
        base.go_to_transport_companies_page()
        tc.filter_transport_company(transport_company_second)
        tc.delete_first_transport_company_on_the_list(transport_company_second)
        tc.check_lack_transport_company_on_the_list(transport_company_second)
        base.refresh_page()
        tc.filter_transport_company(transport_company_first)
        tc.delete_first_transport_company_on_the_list(transport_company_first)
        tc.check_lack_transport_company_on_the_list(transport_company_first)
