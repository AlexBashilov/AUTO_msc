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
    @id('27526')
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
        route.check_filtering_routes(RouteFilter.FIRST_POINT_FILTER, route_point_operations[0]["pointName"])
        route.check_created_route(
            user_credentials["username"], route_name, federal_distinct
        )
        route.delete_first_route()
