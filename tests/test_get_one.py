import requests
from decouple import config

URL_GetOne = config('LOCALHOST_Get_One')


# res = requests.get(URL_GetOne)

def test_get_only_one():
    res = requests.get(URL_GetOne)
    assert res.status_code == 200

