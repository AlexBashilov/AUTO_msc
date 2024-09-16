import allure

from api import routes
from api.models.getVehicle_models import GetVehicleRequestSchema


@allure.step("Отправить GET запрос на ручку /get_vehicle")
def get_vehicle(client, body: GetVehicleRequestSchema):
    allure.attach(body.json(), name="Запрос", attachment_type="JSON")
    response = client.post(routes.Routes.GET_VEHICLE, json=body.dict())
    allure.attach(response.content, name="Ответ", attachment_type="JSON")
    return response
