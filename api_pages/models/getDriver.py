from typing import List
from pydantic import BaseModel


class DriverRequestParams(BaseModel):
    id: int


class GetDriverRequestSchema(BaseModel):
    requestId: str
    params: DriverRequestParams


class DriverData(BaseModel):
    id: int
    surname: str
    name: str
    patronymic: str
    phoneNumber: str
    state: int
    hasTrips: bool
    createdAt: str
    transportCompanyIds: List[int]
    passportDate: str
    passportFullNumber: str
    licenseNumber: str


class Driver(BaseModel):
    Driver: DriverData


class GetDriverResponseSchema(BaseModel):
    requestId: str
    result: Driver


class ErrorMessage(BaseModel):
    message: str


class GetDriverErrorSchema(BaseModel):
    requestId: str
    errors: List[ErrorMessage]
