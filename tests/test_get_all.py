import requests
from decouple import config


URL_GetAll = config('LOCALHOST_Get_All')


# res = requests.get(URL_GetAll)


def test_get_all():
    res = requests.get(URL_GetAll)
    assert res.status_code == 200
