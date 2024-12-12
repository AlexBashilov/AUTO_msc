import allure
import pytest
from allure import title, id
from pages.base_page import Base
from pages.login_page import Login
from pages.route_page import RoutePage
from test_data.error_routes_messages import ErrorRoutesMessages
from test_data.federal_district import FederalDistrict
from test_data.route_operation_type import RouteOperationType
from test_data.shop_list import ShopList
from test_data.test_params.invalid_routes import InvalidRoutes
from test_data.test_params.valid_routes import ValidRoutes


class TestCreateRoute:
    valid_routes = ValidRoutes().list_of_routes_parameters()
    invalid_routes = InvalidRoutes().list_of_invalid_routes_parameters()

    @pytest.mark.parametrize("example", valid_routes)
    def test_create_valid_routes(self, db_connection, driver, example):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)
        route_points = []

        allure.dynamic.title(f'Создание маршрута с {example["name"]}')
        allure.dynamic.id(example["allureID"])
        base.go_to_main_page()
        user_credentials = login.login_to_TMS()
        base.go_to_routes_page()
        route.create_route()
        for point_operation in example["routePointOperation"]:
            route.add_operation_in_route(
                point_operation["pointName"],
                point_operation["operationType"],
                point_operation["unloadPoint"],
            )
            if point_operation["pointName"] not in route_points:
                route_points.append(point_operation["pointName"])
        route.set_federal_district(example["routeDistrict"])
        route_name = route.get_full_route_name(route_points)
        route.delete_route_from_db_by_points(db_connection, route_name)
        route.save_route()
        route.check_created_route(
            user_credentials["username"], route_name, example["routeDistrict"]
        )
        route.delete_first_route()

    @pytest.mark.parametrize("example", invalid_routes)
    def test_create_invalid_routes(self, db_connection, driver, example):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)

        allure.dynamic.title(f'Создание маршрута с {example["name"]}')
        allure.dynamic.id(example["allureID"])
        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_routes_page()
        route.create_route()
        for point_operation in example["routePointOperation"]:
            route.add_operation_in_route(
                point_operation["pointName"],
                point_operation["operationType"],
                point_operation["unloadPoint"],
            )
        route.set_federal_district(example["routeDistrict"])
        route.check_error_message_after_save_route(example["expectedError"])

    @title("Создание маршрута с одной точкой загрузки")
    @id("27549")
    def test_create_route_with_only_one_loading_point(self, db_connection, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)

        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_routes_page()
        route.create_route()
        route.add_operation_in_route(
            ShopList.MSK_DOMODEDOVO_WAREHOUSE, RouteOperationType.LOADING
        )
        route.set_federal_district(FederalDistrict.CFO_DISTRICT)
        route.check_lock_save_button()

    @title("Создание маршрута только с одной точкой разгрузки")
    @id("27627")
    def test_create_route_with_only_one_unloading_point(self, db_connection, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)

        base.go_to_main_page()
        login.login_to_TMS()
        base.go_to_routes_page()
        route.create_route()
        route.set_federal_district(FederalDistrict.CFO_DISTRICT)
        route.check_lock_unload_operation(
            ShopList.MSK_BAGRATION_SHOP, RouteOperationType.UNLOADING
        )

    @title("Создание уже существующего маршрута")
    @id("36446")
    def test_create_exist_route(self, db_connection, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)
        route_points = [ShopList.MSK_DOMODEDOVO_WAREHOUSE, ShopList.MSK_SEVASTOPOL_SHOP]
        federal_distinct = FederalDistrict.CFO_DISTRICT
        route_name = route.get_full_route_name(route_points)
        route.delete_route_from_db_by_points(db_connection, route_name)

        base.go_to_main_page()
        user_credentials = login.login_to_TMS()
        base.go_to_routes_page()
        route.create_route()
        route.add_operation_in_route(route_points[0], RouteOperationType.LOADING)
        route.add_operation_in_route(
            route_points[1], RouteOperationType.UNLOADING, route_points[0]
        )
        route.set_federal_district(federal_distinct)
        route.save_route()
        route.filtering_routes_by_first_points(route_points[0])
        route.filtering_routes_by_last_points(route_points[1])
        route.check_created_route(
            user_credentials["username"], route_name, federal_distinct
        )
        route.create_route()
        route.add_operation_in_route(route_points[0], RouteOperationType.LOADING)
        route.add_operation_in_route(
            route_points[1], RouteOperationType.UNLOADING, route_points[0]
        )
        route.set_federal_district(federal_distinct)
        route.check_error_message_after_save_route(ErrorRoutesMessages.SAME_ROUTE_ERROR)
        route.close_create_route_window()
        route.delete_first_route()

    @title("Создание маршрута на основании существующего маршрута")
    @id("40482")
    def test_create_route_based_on(self, db_connection, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)
        route_point_operations = [
            {
                "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                "operationType": RouteOperationType.LOADING,
                "unloadPoint": None,
            },
            {
                "pointName": ShopList.MSK_VIDNOE_SHOP,
                "operationType": RouteOperationType.UNLOADING,
                "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
            },
        ]
        federal_distinct = FederalDistrict.CFO_DISTRICT
        first_route_points = []

        base.go_to_main_page()
        user_credentials = login.login_to_TMS()
        base.go_to_routes_page()
        route.create_route()
        for point_operation in route_point_operations:
            route.add_operation_in_route(
                point_operation["pointName"],
                point_operation["operationType"],
                point_operation["unloadPoint"],
            )
            first_route_points.append(point_operation["pointName"])
        route.set_federal_district(federal_distinct)
        first_route_name = route.get_full_route_name(first_route_points)
        route.delete_route_from_db_by_points(db_connection, first_route_name)
        route.save_route()
        route.check_created_route(
            user_credentials["username"], first_route_name, federal_distinct
        )
        route.create_route_based_on()
        route.check_open_route(route_point_operations)
        route.delete_operation_in_route_by_number(2)
        route.add_operation_in_route(
            ShopList.MSK_KUBINKA_SHOP,
            RouteOperationType.UNLOADING,
            ShopList.MSK_DOMODEDOVO_WAREHOUSE,
        )
        second_route_points = first_route_points
        second_route_points[1] = ShopList.MSK_KUBINKA_SHOP
        second_route_name = route.get_full_route_name(second_route_points)
        route.delete_route_from_db_by_points(db_connection, second_route_points)
        route.save_route()
        route.check_created_route(
            user_credentials["username"], second_route_name, federal_distinct
        )
        route.delete_first_route()
        route.filtering_routes_by_route_name(first_route_name)
        route.delete_first_route()
