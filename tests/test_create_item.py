import pytest
import requests
import uuid
from internal.api_utils.api_utils import ApiClient
from internal.post_create_item import post_create_items
from internal.models.responseModels import RequestCreateItems



class TestCreateItems:
    @pytest.fixture(scope='class')
    def client(self):
        return ApiClient()
    
    def test_create_item(self, client):
        body = RequestCreateItems(
            item_name=str('fantomas2'),
            guid=str(uuid.uuid4()),
            description=str('opisanie')
        )
        response = post_create_items(client, body)
        print(client)
        assert response.status_code == 201
    
        
        


# def test_get_only_one_new_item(): #попытка написать функцию, которая бы брала данные из функции test_create_item
#     response = requests.post('http://localhost:8080/book_cost_items/create',json=PostParams )
#     response_json = response.json()
#     print(response_json['ID'])
#     assert response.status_code == 201

def test_delete_item():
    pass