import requests


res = requests.get('http://localhost:8080/book_cost_items/get_all')


def test_res():
    assert res.status_code == 200
