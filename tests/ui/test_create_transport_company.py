import allure
import pytest

from pages.base_page import Base
from pages.login_page import Login
from pages.transport_companies_page import TransportCompaniesPage
from testData.invalid_transport_companies import InvalidTransportCompanies
from testData.valid_transport_companies import ValidTransportCompanies


class TestCreateTransportCompany:
    validTransportCompanies = ValidTransportCompanies().list_of_transport_companies_parameters()
    invalidTransportCompanies = InvalidTransportCompanies().list_of_invalid_transport_companies_parameters()

    @pytest.mark.parametrize("example", validTransportCompanies)
    def test_create_transport_company_and_delete(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)

        allure.dynamic.title(example['name'])
        allure.dynamic.id(example['allureID'])
        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_transport_companies_page()
        tc.create_transport_company()
        tc.fill_transport_company(example)
        tc.save_transport_company()
        tc.filter_transport_company(example)
        tc.delete_first_transport_company_on_the_list(example)
        tc.check_lack_transport_company_on_the_list(example)

    @pytest.mark.parametrize("example", invalidTransportCompanies)
    def test_create_invalid_transport_company(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)

        allure.dynamic.title(example['name'])
        allure.dynamic.id(example['allureID'])
        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_transport_companies_page()
        tc.create_transport_company()
        tc.fill_transport_company(example)
        tc.check_error_message_after_save_transport_company(example['error'])
