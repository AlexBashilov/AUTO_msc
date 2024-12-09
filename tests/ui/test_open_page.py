import allure
from pages.base_page import Base
from pages.login_page import Login
from pages.route_page import RoutePage
from pages.transport_companies_page import TransportCompaniesPage
from pages.trips_page import TripsPage


class TestOpenPage:
    @allure.id(35346)
    @allure.title('Проверка открытия страницы "Маршруты"')
    def test_open_route_page(self, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)

        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_routes_page()
        route.check_route_page_elements()

    @allure.id(35511)
    @allure.title('Проверка открытия страницы "Рейсы"')
    def test_open_trips_page(self, driver):
        base = Base(driver)
        login = Login(driver)
        trips = TripsPage(driver)

        base.go_to_main_page()
        login.login_to_TMS()
        trips.check_trips_page_elements()

    @allure.id(35512)
    @allure.title('Проверка открытия страницы "Транспортные компании"')
    def test_open_transport_companies_page(self, driver):
        base = Base(driver)
        login = Login(driver)
        transport = TransportCompaniesPage(driver)

        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_transport_companies_page()
        transport.check_transport_companies_page_elements()
