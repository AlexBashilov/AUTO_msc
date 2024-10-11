from pydantic import BaseModel
from internal import routes

def post_create_items(client, body: BaseModel):
    response = client.post(routes.Routes.createItemsRoute, json=body.dict())
    return response
