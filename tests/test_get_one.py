import requests
#import pytest
#from tests.test_create_item import response

#otvet = response.request.body[id]

res = requests.get('http://localhost:8080/book_cost_items/get_only_one/60')

#@pytest.mark.parametrize
def test_get_only_one():
    assert res.status_code == 200

