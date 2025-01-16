from pydantic import BaseModel

"""
Схемы запроса для ручки createDriver
"""


class CreateDriverRequestParams(BaseModel):
    transportCompanyIds: list[int] | None = None
    surname: str | None = None
    name: str | None = None
    patronymic: str | None = None
    phoneNumber: str | None = None
    passportDate: str | None = None
    passportFullNumber: str | None = None
    licenseNumber: str | None = None


class CreateDriverRequestSchema(BaseModel):
    params: CreateDriverRequestParams
    requestId: str = "autotest"


"""
Схемы ответа для ручки createDriver
"""


class DriverID(BaseModel):
    id: int


class CreateDriverResponseSchema(BaseModel):
    result: DriverID
    requestId: str = "autotest"


"""
Схемы ошибок для ручки createDriver
"""


class ErrorData(BaseModel):
    anotherDriverId: int | None = None


class ErrorMessage(BaseModel):
    data: ErrorData | None = None
    message: str


class CreateDriverErrorSchema(BaseModel):
    requestId: str = "autotest"
    errors: list[ErrorMessage]


class CreateDriverRequiredParamsErrorSchema(BaseModel):
    code: int
    message: str
