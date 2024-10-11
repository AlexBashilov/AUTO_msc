import requests
from decouple import config

URL_GetOne = config('LOCALHOST_Get_One')


res = requests.get(URL_GetOne)

def test_get_only_one():
    assert res.status_code == 200

