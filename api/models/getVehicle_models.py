from typing import List

from pydantic import BaseModel


class VehicleData(BaseModel):
    id: int
    transportCompanyIds: List[int]
    typeId: int
    number: str
    brandId: int
    weightCapacity: int | None
    hasActiveTrip: bool


class Vehicle(BaseModel):
    vehicle: VehicleData


class GetVehicleResponseSchema(BaseModel):
    requestId: str
    result: Vehicle


class ErrorMessage(BaseModel):
    message: str


class GetVehicleErrorSchema(BaseModel):
    requestId: str
    errors: List[ErrorMessage]
