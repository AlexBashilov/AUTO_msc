import requests
#from tests.settings import LOCALHOST

res = requests.get('http://localhost:8080/book_cost_items/get_all')


def test_get_all():
    assert res.status_code == 200
