import allure
import pytest

from pages.base_page import Base
from pages.login_page import Login
from pages.route_page import RoutePage
from test_data.test_params.valid_routes import ValidRoutes


class TestCreateRoute:
    valid_routes = ValidRoutes().list_of_routes_parameters()
    # invalid_routes = InvalidDRoutes().list_of_invalid_routes_parameters()

    @pytest.mark.parametrize("example", valid_routes)
    def test_create_valid_routes(self, driver, example):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)
        route_points = []

        allure.dynamic.title(example["name"])
        allure.dynamic.id(example["allureID"])
        base.go_to_main_page()
        user_credentials = login.login_to_TMS()
        base.go_to_routes_page()
        route.create_route()
        for point_operation in example['routePointOperation']:
            route.add_operation_in_route(point_operation['pointName'], point_operation['operationType'], point_operation['unloadPoint'])
            if point_operation['pointName'] not in route_points:
                    route_points.append(point_operation['pointName'])
        route.set_federal_district(example['routeDistrict'])
        route_name = route.get_full_route_name(route_points)
        route.delete_route_from_db_by_points(route_name)
        route.save_route()
        route.check_created_route(user_credentials['login'], route_name, example['routeDistrict'])
        route.delete_first_route()