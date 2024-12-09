from enum import Enum


class RouteOperationType(str, Enum):
    """
    Типы операций в маршрутах
    """

    LOADING = "Загрузка"
    UNLOADING = "Разгрузка"

    def __str__(self) -> str:
        return self.value
