from typing import List
import uuid
from pydantic import BaseModel


class GetAllItemsDetailsResponse(BaseModel):
    description: str
    guid: str
    id: int
    item_name: str


class GetAllItemsResponseSchema(BaseModel):
    details: str
    result: List[GetAllItemsDetailsResponse]



class ErrorMessage(BaseModel):
    message: str


class GetDriverErrorSchema(BaseModel):
    requestId: str
    errors: List[ErrorMessage]
