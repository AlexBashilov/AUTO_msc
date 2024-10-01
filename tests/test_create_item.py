import requests
#import pytest
#import names
#from settings import LOCALHOST
import uuid

#PostParams = dict(item_name= 'тестовые данные из питона' , guid= str(uuid.uuid4()) , description= 'тестовые данные из питона')
PostParams = {
    'item_name': 'Kiska',
    'guid' : str(uuid.uuid4()),
    'description' : 'Opisani piton',
    }
res = requests.post('http://localhost:8080/book_cost_items/create',json=PostParams )
response = res.json()
print(response)
#print(response)
#@pytest.mark.parametrize(
#    'item_name, guid, description',
#    [PostParams.item_name, PostParams.guid, PostParams.description]
#    )
def test_create_item():
    assert res.status_code == 201
    