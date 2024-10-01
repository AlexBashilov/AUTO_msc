import requests

import uuid


PostParams = {
    'item_name': 'Kiska5',
    'guid' : str(uuid.uuid4()),
    'description' : 'Opisani piton',
    }
#res = requests.post('http://localhost:8080/book_cost_items/create',json=PostParams )
#response = res.json()
#print(response)

def test_create_item():
    res = requests.post('http://localhost:8080/book_cost_items/create',json=PostParams )
    assert res.status_code == 201
    
    
#print(response)
#@pytest.mark.parametrize(
#    'item_name, guid, description',
#    [PostParams.item_name, PostParams.guid, PostParams.description]
#    )