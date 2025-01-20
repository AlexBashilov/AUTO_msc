from typing import List
#import uuid
from pydantic import BaseModel

class GetOneItemsByIDDetailsResponse(BaseModel):
    id: int
    item_name: str
    guid: str
    description: str


class GetOneItemsByIDResponseSchema(BaseModel):
    details: str
    result: GetOneItemsByIDDetailsResponse