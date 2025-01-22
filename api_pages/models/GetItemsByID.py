from typing import List
#import uuid
from pydantic import BaseModel

class GetOneItemParams(BaseModel):
    id: int

class GetOneItemsByIDDetailsResponse(BaseModel):
    id: int
    item_name: str
    guid: str
    description: str


class GetOneItemsByIDResponseSchema(BaseModel):
    result: str
    details: GetOneItemsByIDDetailsResponse