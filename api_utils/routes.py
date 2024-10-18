from enum import Enum


class Routes(str, Enum):
    GET_VEHICLE = '/getVehicle'
    GET_VEHICLES = '/getVehicles'

    GET_DRIVER = '/getDriver'
    GET_DRIVERS = '/getDrivers'

    def __str__(self) -> str:
        return self.value
