import pytest

from pages.base_page import Base
from pages.login_page import Login
from pages.transport_companies_page import TransportCompaniesPage
from pages.drivers_page import DriversPage

from test_data.transport_companies import TransportCompanies
from test_data.test_params.valid_drivers import ValidDrivers
from test_data.test_params.invalid_drivers import InvalidDrivers
from test_data.error_drivers_messages import ErrorDriversMessages
from test_data.drivers import Drivers
from faker import Faker


class TestCreateDriver:
    valid_drivers = ValidDrivers().list_of_drivers_parameters()
    invalid_drivers = InvalidDrivers().list_of_invalid_drivers_parameters()
    same_parameters_drivers = InvalidDrivers().list_of_same_drivers_parameters()

    @pytest.mark.parametrize("example", valid_drivers)
    def test_create_valid_driver(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)
        drivers = DriversPage(driver)
        transport_company = TransportCompanies().generate_random_tc(example["name"])

        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_transport_companies_page()
        tc.create_transport_company()
        tc.fill_transport_company(transport_company)
        tc.save_transport_company()
        tc.filter_transport_company(transport_company)
        tc.go_to_first_transport_company_on_the_list()
        drivers.goToDriversTab()
        drivers.createDriver()
        drivers.fillDriver(example)
        drivers.saveDriver()
        drivers.filterDriverByPhoneNumber(example)
        drivers.deleteFirstDriverOnTheList(example)
        drivers.checkLackDriverOnTheList(example)
        base.go_to_transport_companies_page()
        tc.filter_transport_company(transport_company)
        tc.delete_first_transport_company_on_the_list(transport_company)
        tc.check_lack_transport_company_on_the_list(transport_company)

    @pytest.mark.parametrize("example", invalid_drivers)
    def test_create_invalid_driver(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)
        drivers = DriversPage(driver)
        transport_company = TransportCompanies().generate_random_tc(example["name"])

        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_transport_companies_page()
        tc.create_transport_company()
        tc.fill_transport_company(transport_company)
        tc.save_transport_company()
        tc.filter_transport_company(transport_company)
        tc.go_to_first_transport_company_on_the_list()
        drivers.goToDriversTab()
        drivers.createDriver()
        drivers.fillDriver(example)
        drivers.checkDisableSaveDriverButton()
        base.close_info_modal()
        base.go_to_transport_companies_page()
        tc.filter_transport_company(transport_company)
        tc.delete_first_transport_company_on_the_list(transport_company)
        tc.check_lack_transport_company_on_the_list(transport_company)

    @pytest.mark.parametrize("example", same_parameters_drivers)
    def test_create_driver_with_same_parameters(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)
        drivers = DriversPage(driver)
        transport_company = TransportCompanies().generate_random_tc(example["name"])
        fake = Faker("ru_RU")


        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_transport_companies_page()
        tc.create_transport_company()
        tc.fill_transport_company(transport_company)
        tc.save_transport_company()
        tc.filter_transport_company(transport_company)
        tc.go_to_first_transport_company_on_the_list()
        drivers.goToDriversTab()
        drivers.createDriver()
        drivers.fillDriver(example)
        drivers.saveDriver()
        if example["error"] == ErrorDriversMessages.SAME_PASSPORT_ERROR:
            example[Drivers.LICENSE_NUMBER] = fake.random_number(digits=10)
        if example["error"] == ErrorDriversMessages.SAME_DRIVER_LICENCE_ERROR:
            example[Drivers.PASSPORT_NUMBER] = fake.passport_number()
        drivers.createDriver()
        drivers.fillDriver(example)
        drivers.checkErrorMessageAfterSaveDriver(example["error"])
        base.close_info_modal()
        drivers.filterDriverByPhoneNumber(example)
        drivers.deleteFirstDriverOnTheList(example)
        drivers.checkLackDriverOnTheList(example)
        base.go_to_transport_companies_page()
        tc.filter_transport_company(transport_company)
        tc.delete_first_transport_company_on_the_list(transport_company)
        tc.check_lack_transport_company_on_the_list(transport_company)
