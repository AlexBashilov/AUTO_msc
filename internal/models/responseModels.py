from pydantic import BaseModel


class ResponseCreateItems(BaseModel):
    id: int
    item_name: str
    guid: str
    description: str
    
class RequestCreateItems(BaseModel):
    item_name: str
    guid: str
    description: str