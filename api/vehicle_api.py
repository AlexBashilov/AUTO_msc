import allure
from allure_commons.types import AttachmentType
from pydantic import BaseModel

from api import routes


@allure.step("Отправить GET запрос на ручку /get_vehicle")
def get_vehicle(client, body: BaseModel):
    response = client.post(routes.Routes.GET_VEHICLE, json=body.dict())
    allure.attach(response.content, name="Ответ", attachment_type=AttachmentType.JSON)
    return response
