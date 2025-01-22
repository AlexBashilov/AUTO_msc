from typing import List
import uuid
from pydantic import BaseModel


class GetAllItemsDetailsResponse(BaseModel):
    description: str
    guid: str
    id: int
    item_name: str


class AllItems(BaseModel):
    AllItems: GetAllItemsDetailsResponse


class GetAllItemsResponseSchema(BaseModel):
    details: AllItems
    result: str



class ErrorMessage(BaseModel):
    message: str


class GetDriverErrorSchema(BaseModel):
    requestId: str
    errors: List[ErrorMessage]
