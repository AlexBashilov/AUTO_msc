import requests
from pydantic import BaseModel
from internal import routes
from decouple import config


URL_GetOne = config('LOCALHOST')

def post_create_items(client, body: BaseModel):
    response = client.post(URL_GetOne + routes.Routes.createItemsRoute, json=body.dict())
    return response
