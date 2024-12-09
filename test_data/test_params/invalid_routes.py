from typing import List

from test_data.error_routes_messages import ErrorRoutesMessages
from test_data.federal_district import FederalDistrict
from test_data.route_operation_type import RouteOperationType
from test_data.shop_list import ShopList


class InvalidRoutes:
    def list_of_invalid_routes_parameters(self) -> List[dict]:
        return [
            {
                "name": "двумя точками загрузки и одной точкой разгрузки",
                "allureID": "27599",
                "expectedError": ErrorRoutesMessages.DIFFERENT_OPERATION_ERROR,
                "routeDistrict": FederalDistrict.CFO_DISTRICT,
                "routePointOperation": [
                    {
                        "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                        "operationType": RouteOperationType.LOADING,
                        "unloadPoint": None,
                    },
                    {
                        "pointName": ShopList.NN_DOSKINO_WAREHOUSE,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                    },
                    {
                        "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                        "operationType": RouteOperationType.LOADING,
                        "unloadPoint": None,
                    },
                ],
            },
            {
                "name": "одной точкой загрузки и двумя точками разгрузки",
                "allureID": "27548",
                "expectedError": ErrorRoutesMessages.DIFFERENT_OPERATION_ERROR,
                "routeDistrict": FederalDistrict.CFO_DISTRICT,
                "routePointOperation": [
                    {
                        "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                        "operationType": RouteOperationType.LOADING,
                        "unloadPoint": None,
                    },
                    {
                        "pointName": ShopList.NN_DOSKINO_WAREHOUSE,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                    },
                    {
                        "pointName": ShopList.KAZAN_WAREHOUSE,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                    },
                ],
            },
            {
                "name": "несвязными операциями (есть 2 загрузки, но используется только 1)",
                "allureID": "40871",
                "expectedError": ErrorRoutesMessages.UNRELATED_OPERATION_ERROR,
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
                        "pointName": ShopList.NN_DOSKINO_WAREHOUSE,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                    },
                    {
                        "pointName": ShopList.KAZAN_WAREHOUSE,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                    },
                ],
            },
            {
                "name": "зацикленными операциями (загрузка в одном и том же складе, после разгрузки)",
                "allureID": "40869",
                "expectedError": ErrorRoutesMessages.LOOP_OPERATION_ERROR,
                "routeDistrict": FederalDistrict.CFO_DISTRICT,
                "routePointOperation": [
                    {
                        "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                        "operationType": RouteOperationType.LOADING,
                        "unloadPoint": None,
                    },
                    {
                        "pointName": ShopList.KAZAN_WAREHOUSE,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                    },
                    {
                        "pointName": ShopList.KAZAN_WAREHOUSE,
                        "operationType": RouteOperationType.LOADING,
                        "unloadPoint": None,
                    },
                    {
                        "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": ShopList.KAZAN_WAREHOUSE,
                    },
                ],
            },
            {
                "name": "точками без лог.цепочек",
                "allureID": "40897",
                "expectedError": ErrorRoutesMessages.LOG_CHAIN_ERROR,
                "routeDistrict": FederalDistrict.CFO_DISTRICT,
                "routePointOperation": [
                    {
                        "pointName": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                        "operationType": RouteOperationType.LOADING,
                        "unloadPoint": None,
                    },
                    {
                        "pointName": ShopList.MRK_ATLANTIC_SHOP,
                        "operationType": RouteOperationType.UNLOADING,
                        "unloadPoint": ShopList.MSK_DOMODEDOVO_WAREHOUSE,
                    },
                ],
            },
        ]
