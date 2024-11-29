import allure
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


class TestCreateRoute:
    valid_routes = ValidRoutes().list_of_routes_parameters()
    invalid_routes = InvalidDRoutes().list_of_invalid_routes_parameters()

    @pytest.mark.parametrize("example", valid_routes)
    def test_create_valid_routes(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        tc = TransportCompaniesPage(driver)
        drivers = DriversPage(driver)
        transport_company = TransportCompanies().generate_random_tc(example["name"])

        allure.dynamic.title(example["name"])
        allure.dynamic.id(example["allureID"])
        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_routes_page()

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

        I->setTestNameInAllure('Создание маршрута с ' . example['name'])
        I->setAllureID(example['allureID'])
        routePoints = []

        base->goToTMSMainPage()
        userCredentials = authentication->loginToTMS()
        base->goToRoutesPage()
        routePage->createRoute()
        foreach (example['routePointOperation'] as pointOperation) {
            routePage->addOperationInRoute(pointOperation['pointName'], pointOperation['operationType'], pointOperation['unloadPoint'])
            if (!in_array(pointOperation['pointName'], routePoints))
            {
                routePoints[] = pointOperation['pointName']
            }
        }
        routePage->setFederalDistrict(example['routeDistrict'])
        routeName = routePage->getFullRouteName(routePoints)
        routePage->deleteRouteFromDbByPoints(routeName)
        routePage->saveRoute()
        routePage->checkCreatedRoute(userCredentials['login'], routeName, example['routeDistrict'])
        routePage->deleteFirstRoute()