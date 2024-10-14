import allure
import pytest

from pages.base_page import Base
from pages.login_page import Login
from pages.transport_companies_page import TransportCompaniesPage
from pages.drivers_page import DriversPage

from testData.transport_companies import TransportCompanies
from testData.valid_drivers import ValidDrivers
from testData.invalid_drivers import InvalidDrivers
from testData.error_drivers_messages import ErrorDriversMessages
from testData.drivers import Drivers
from faker import Faker


class TestCreateDriver:
    validDrivers = ValidDrivers().list_of_drivers_parameters()
    invalidDrivers = InvalidDrivers().list_of_invalid_drivers_parameters()
    sameParametersDrivers = InvalidDrivers().list_of_same_drivers_parameters()

    @pytest.mark.parametrize("example", validDrivers)
    def test_create_valid_driver(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)
        drivers = DriversPage(driver)
        transport_company = TransportCompanies().generate_random_tc(example['name'])

        allure.dynamic.title(example['name'])
        allure.dynamic.id(example['allureID'])
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

    @pytest.mark.parametrize("example", invalidDrivers)
    def test_create_invalid_driver(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)
        drivers = DriversPage(driver)
        transport_company = TransportCompanies().generate_random_tc(example['name'])

        allure.dynamic.title(example['name'])
        allure.dynamic.id(example['allureID'])
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

    @pytest.mark.parametrize("example", sameParametersDrivers)
    def test_create_driver_with_same_parameters(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)
        drivers = DriversPage(driver)
        transport_company = TransportCompanies().generate_random_tc(example['name'])
        fake = Faker('ru_RU')

        allure.dynamic.title(example['name'])
        allure.dynamic.id(example['allureID'])
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
        if example['error'] == ErrorDriversMessages.SAME_PASSPORT_ERROR:
            example[Drivers.LICENSE_NUMBER] = fake.random_number(digits=10)
        if example['error'] == ErrorDriversMessages.SAME_DRIVER_LICENCE_ERROR:
            example[Drivers.PASSPORT_NUMBER] = fake.passport_number()
        drivers.createDriver()
        drivers.fillDriver(example)
        drivers.checkErrorMessageAfterSaveDriver(example['error'])
        base.close_info_modal()
        drivers.filterDriverByPhoneNumber(example)
        drivers.deleteFirstDriverOnTheList(example)
        drivers.checkLackDriverOnTheList(example)
        base.go_to_transport_companies_page()
        tc.filter_transport_company(transport_company)
        tc.delete_first_transport_company_on_the_list(transport_company)
        tc.check_lack_transport_company_on_the_list(transport_company)
