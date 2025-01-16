from allure import title, id
from pages.base_page import Base
from pages.login_page import Login
from pages.route_page import RoutePage
from test_data.federal_district import FederalDistrict
from test_data.route_filter import RouteFilter
from test_data.route_operation_type import RouteOperationType
from test_data.shop_list import ShopList


class TestFiltrationRoute:
    @title("Поиск маршрута по первой точке")
    @id("27526")
    def test_check_filtration_by_first_point(self, db_connection, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)
        route_point_operations = [
            {
                "pointName": ShopList.PERM_WAREHOUSE,
                "operationType": RouteOperationType.LOADING,
                "unloadPoint": None,
            },
            {
                "pointName": ShopList.PERM_UINSKAYA_SHOP,
                "operationType": RouteOperationType.UNLOADING,
                "unloadPoint": ShopList.PERM_WAREHOUSE,
            },
        ]
        federal_distinct = FederalDistrict.CFO_DISTRICT
        route_name = route.get_full_route_name(route_point_operations)
        route.delete_route_from_db_by_points(db_connection, route_name)

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
        route.set_federal_district(federal_distinct)
        route.save_route()
        route.filtering_routes_by_first_points(route_point_operations[0]["pointName"])
        route.check_filtering_routes(
            RouteFilter.FIRST_POINT_FILTER, route_point_operations[0]["pointName"]
        )
        route.check_created_route(user_credentials["username"], route_name, federal_distinct)
        route.delete_first_route()

    @title("Поиск маршрута по любой точке")
    @id("27349")
    def test_check_filtration_by_any_point(self, db_connection, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)
        route_point_operations = [
            {
                "pointName": ShopList.KAZAN_WAREHOUSE,
                "operationType": RouteOperationType.LOADING,
                "unloadPoint": None,
            },
            {
                "pointName": ShopList.KAZAN_WAREHOUSE,
                "operationType": RouteOperationType.LOADING,
                "unloadPoint": None,
            },
            {
                "pointName": ShopList.KIR_POPOVA_SHOP,
                "operationType": RouteOperationType.UNLOADING,
                "unloadPoint": "1 " + ShopList.KAZAN_WAREHOUSE,
            },
            {
                "pointName": ShopList.KIR_MOSCOW_SHOP,
                "operationType": RouteOperationType.UNLOADING,
                "unloadPoint": "2 " + ShopList.KAZAN_WAREHOUSE,
            },
        ]
        federal_distinct = FederalDistrict.CFO_DISTRICT
        route_name = route.get_full_route_name(route_point_operations)
        route.delete_route_from_db_by_points(db_connection, route_name)

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
        route.set_federal_district(federal_distinct)
        route.save_route()
        route.filtering_routes_by_any_points(route_point_operations[2]["pointName"])
        route.check_filtering_routes(
            RouteFilter.ANY_POINT_FILTER, route_point_operations[2]["pointName"]
        )
        route.check_created_route(user_credentials["username"], route_name, federal_distinct)
        route.delete_first_route()

    @title("Поиск маршрута по последней точке")
    @id("27540")
    def test_check_filtration_by_last_point(self, db_connection, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)
        route_point_operations = [
            {
                "pointName": ShopList.KAZAN_WAREHOUSE,
                "operationType": RouteOperationType.LOADING,
                "unloadPoint": None,
            },
            {
                "pointName": ShopList.KAZAN_WAREHOUSE,
                "operationType": RouteOperationType.LOADING,
                "unloadPoint": None,
            },
            {
                "pointName": ShopList.KIR_WORCA_SHOP,
                "operationType": RouteOperationType.UNLOADING,
                "unloadPoint": "1 " + ShopList.KAZAN_WAREHOUSE,
            },
            {
                "pointName": ShopList.KIR_PROFSOUZE_SHOP,
                "operationType": RouteOperationType.UNLOADING,
                "unloadPoint": "2 " + ShopList.KAZAN_WAREHOUSE,
            },
        ]
        federal_distinct = FederalDistrict.CFO_DISTRICT
        route_name = route.get_full_route_name(route_point_operations)
        route.delete_route_from_db_by_points(db_connection, route_name)

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
        route.set_federal_district(federal_distinct)
        route.save_route()
        route.filtering_routes_by_last_points(route_point_operations[-1]["pointName"])
        route.check_filtering_routes(
            RouteFilter.LAST_POINT_FILTER, route_point_operations[-1]["pointName"]
        )
        route.check_created_route(user_credentials["username"], route_name, federal_distinct)
        route.delete_first_route()

    @title("Поиск маршрута по названию маршрута")
    @id("27505")
    def test_check_filtration_by_route_name(self, db_connection, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)
        route_point_operations = [
            {
                "pointName": ShopList.KAZAN_WAREHOUSE,
                "operationType": RouteOperationType.LOADING,
                "unloadPoint": None,
            },
            {
                "pointName": ShopList.KIR_MIXEEVA_SHOP,
                "operationType": RouteOperationType.UNLOADING,
                "unloadPoint": ShopList.KAZAN_WAREHOUSE,
            },
        ]
        federal_distinct = FederalDistrict.CFO_DISTRICT
        route_name = route.get_full_route_name(route_point_operations)
        route.delete_route_from_db_by_points(db_connection, route_name)

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
        route.set_federal_district(federal_distinct)
        route.save_route()
        route.filtering_routes_by_route_name(route_name)
        route.check_filtering_routes(RouteFilter.ROUTE_NAME_FILTER, route_name)
        route.check_created_route(user_credentials["username"], route_name, federal_distinct)
        route.delete_first_route()

    @title("Очистка всех фильтров")
    @id("27716")
    def test_clear_all_filters(self, db_connection, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)
        route_point_operations = [
            {
                "pointName": ShopList.PERM_WAREHOUSE,
                "operationType": RouteOperationType.LOADING,
                "unloadPoint": None,
            },
            {
                "pointName": ShopList.PERM_LASVINSKAYA_SHOP,
                "operationType": RouteOperationType.UNLOADING,
                "unloadPoint": ShopList.PERM_WAREHOUSE,
            },
        ]
        federal_distinct = FederalDistrict.CFO_DISTRICT
        route_name = route.get_full_route_name(route_point_operations)
        route.delete_route_from_db_by_points(db_connection, route_name)

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
        route.set_federal_district(federal_distinct)
        route.save_route()
        route.filtering_routes_by_first_points(route_point_operations[0]["pointName"])
        route.filtering_routes_by_any_points(route_point_operations[0]["pointName"])
        route.filtering_routes_by_last_points(route_point_operations[-1]["pointName"])
        route.check_created_route(user_credentials["username"], route_name, federal_distinct)
        route.clear_route_filter()
        route.filtering_routes_by_route_name(route_name)
        route.delete_first_route()

    @title("Поиск маршрутов только с активными шаблонами")
    @id("27541")
    def test_check_filtration_by_active_route(self, db_connection, driver):
        base = Base(driver)
        login = Login(driver)
        route = RoutePage(driver)
        route_point_operations = [
            {
                "pointName": ShopList.PERM_WAREHOUSE,
                "operationType": RouteOperationType.LOADING,
                "unloadPoint": None,
            },
            {
                "pointName": ShopList.PERM_OVERYATSKAYA_SHOP,
                "operationType": RouteOperationType.UNLOADING,
                "unloadPoint": ShopList.PERM_WAREHOUSE,
            },
        ]
        federal_distinct = FederalDistrict.CFO_DISTRICT
        route_name = route.get_full_route_name(route_point_operations)
        route.delete_route_from_db_by_points(db_connection, route_name)

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
        route.set_federal_district(federal_distinct)
        route.save_route()
        route.check_created_route(user_credentials["username"], route_name, federal_distinct)
        route.filtering_routes_by_activity(True)
        route.check_empty_route()
        route.filtering_routes_by_activity(False)
        route.check_created_route(user_credentials["username"], route_name, federal_distinct)
        route.delete_first_route()
