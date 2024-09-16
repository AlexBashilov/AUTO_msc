import allure

from api import routes
from api.models.getVehicle_models import GetVehicleRequestSchema


@allure.step("Отправить GET запрос на ручку /get_vehicle")
def get_vehicle(client, body: GetVehicleRequestSchema):
    allure.attach(body, name="Запрос")
    response = client.post(routes.Routes.GET_VEHICLE, json=body.dict())
    allure.attach(response, name="Ответ")
    return response
