from enum import Enum


class Routes(str, Enum):
    """
    Все RPС ручки
    """

    GET_VEHICLE = "/getVehicle"
    GET_VEHICLES = "/getVehicles"
    CREATE_DRIVER = "/createDriver"
    GET_DRIVER = "/getDriver"
    GET_DRIVERS = "/getDrivers"

    def __str__(self) -> str:
        return self.value
