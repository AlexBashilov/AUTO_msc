from enum import Enum


class RouteFilter(str, Enum):
    """
    Все фильтры на сранице маршрутов
    """

    FIRST_POINT_FILTER = "Поиск по первой точке"
    ANY_POINT_FILTER = "Поиск по любой точке"
    LAST_POINT_FILTER = "Поиск по последней точке"
    ROUTE_NAME_FILTER = "Поиск по названию маршрута"

    def __str__(self) -> str:
        return self.value
