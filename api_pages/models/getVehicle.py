from typing import List, Optional
from pydantic import BaseModel


class VehicleRequestParams(BaseModel):
    id: int


class GetVehicleRequestSchema(BaseModel):
    requestId: str
    params: VehicleRequestParams


class VehicleData(BaseModel):
    id: int
    transportCompanyIds: Optional[List[int]] = None
    typeId: int
    number: str
    brandId: int
    model: Optional[str] = None
    ownershipTypeId: Optional[int] = None
    capacityTypeId: Optional[int] = None
    capacityVolume: Optional[int] = None
    cargoBodyTypeId: Optional[int] = None
    weightCapacity: Optional[float] = None
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
