from enum import Enum


class Routes(str, Enum):
    GET_VEHICLE = '/getVehicle'
    GET_VEHICLES = '/getVehicles'

    def __str__(self) -> str:
        return self.value
