from typing import List
from test_data.federal_district import FederalDistrict
from test_data.route_operation_type import RouteOperationType
from test_data.shop_list import ShopList


class ValidRoutes:
    def list_of_routes_parameters(self) -> List[dict]:
        return [
            # {
            #     "name": "одна точка загрузки и одна точка разгрузки",
            #     "allureID": "35927",
            #     "firstRoutePoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
            #     "lastRoutePoint": ShopList.KVR_LENINA_SHOP,
            #     "routeDistrict": FederalDistrict.CFO_DISTRICT,
            #     "routePointOperation": [
            #         {
            #             "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
            #             "operationType": RouteOperationType.LOADING,
            #             "unloadPoint": None,
            #         },
            #         {
            #             "pointName": ShopList.KVR_LENINA_SHOP,
            #             "operationType": RouteOperationType.UNLOADING,
            #             "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
            #         },
            #     ],
            # },
            # {
            #     "name": "две точки загрузки и две точки разгрузки",
            #     "allureID": "27547",
            #     "firstRoutePoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
            #     "lastRoutePoint": ShopList.KIR_GORKOGO_SHOP,
            #     "routeDistrict": FederalDistrict.CFO_DISTRICT,
            #     "routePointOperation": [
            #         {
            #             "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
            #             "operationType": RouteOperationType.LOADING,
            #             "unloadPoint": None,
            #         },
            #         {
            #             "pointName": ShopList.KAZAN_WAREHOUSE,
            #             "operationType": RouteOperationType.UNLOADING,
            #             "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
            #         },
            #         {
            #             "pointName": ShopList.KAZAN_WAREHOUSE,
            #             "operationType": RouteOperationType.LOADING,
            #             "unloadPoint": None,
            #         },
            #         {
            #             "pointName": ShopList.KIR_GORKOGO_SHOP,
            #             "operationType": RouteOperationType.UNLOADING,
            #             "unloadPoint": ShopList.KAZAN_WAREHOUSE,
            #         },
            #     ],
            # },
            # {
            #     "name": "три точки загрузки(разные) и три точки разгрузки(разные)",
            #     "allureID": "27601",
            #     "firstRoutePoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
            #     "lastRoutePoint": ShopList.MRK_ATLANTIC_SHOP,
            #     "routeDistrict": FederalDistrict.CFO_DISTRICT,
            #     "routePointOperation": [
            #         {
            #             "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
            #             "operationType": RouteOperationType.LOADING,
            #             "unloadPoint": None,
            #         },
            #         {
            #             "pointName": ShopList.SPB_WAREHOUSE,
            #             "operationType": RouteOperationType.UNLOADING,
            #             "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
            #         },
            #         {
            #             "pointName": ShopList.SPB_WAREHOUSE,
            #             "operationType": RouteOperationType.LOADING,
            #             "unloadPoint": None,
            #         },
            #         {
            #             "pointName": ShopList.MRK_WAREHOUSE,
            #             "operationType": RouteOperationType.UNLOADING,
            #             "unloadPoint": ShopList.SPB_WAREHOUSE,
            #         },
            #         {
            #             "pointName": ShopList.MRK_WAREHOUSE,
            #             "operationType": RouteOperationType.LOADING,
            #             "unloadPoint": None,
            #         },
            #         {
            #             "pointName": ShopList.MRK_ATLANTIC_SHOP,
            #             "operationType": RouteOperationType.UNLOADING,
            #             "unloadPoint": ShopList.MRK_WAREHOUSE,
            #         },
            #     ],
            # },
            {
                "name": "три точки загрузки(одинаковые) и три точки разгрузки(разные)",
                "allureID": "27604",
                "firstRoutePoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                "lastRoutePoint": ShopList.MSK_KUBINKA_SHOP,
                "routeDistrict": FederalDistrict.CFO_DISTRICT,
                "routePointOperation": [
                    {
                        "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                        "operationType": RouteOperationType.LOADING,
                        "unloadPoint": None,
                    },
                    {
                        "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                        "operationType": RouteOperationType.LOADING,
                        "unloadPoint": None,
                    },
                    {
                        "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                        "operationType": RouteOperationType.LOADING,
                        "unloadPoint": None,
                    },
                    {
                        "pointName": ShopList.MSK_BAGRATION_SHOP,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": "1 " + ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                    },
                    {
                        "pointName": ShopList.MSK_VIDNOE_SHOP,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": "2 " + ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                    },
                    {
                        "pointName": ShopList.MSK_KUBINKA_SHOP,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": "3 " + ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                    },
                ],
            },
        ]
