from api import routes


def get_vehicle(client, body):
    return client.post(routes.Routes.GET_VEHICLE, json=body)
