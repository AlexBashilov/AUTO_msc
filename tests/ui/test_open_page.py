from pages.base_page import Base
from pages.login_page import Login
from pages.route_page import RoutePage
from pages.transport_companies_page import TransportCompaniesPage
from pages.trips_page import TripsPage


class TestOpenPage:
    def test_open_route_page(self, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)

        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_routes_page()
        route.check_route_page_elements()


    def test_open_trips_page(self, driver):
        base = Base(driver)
        login = Login(driver)
        trips = TripsPage(driver)

        base.go_to_main_page()
        login.login_to_TMS()
        trips.check_trips_page_elements()

    def test_open_transport_companies_page(self, driver):
        base = Base(driver)
        login = Login(driver)
        transport = TransportCompaniesPage(driver)

        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_transport_companies_page()
        transport.check_transport_companies_page_elements()
