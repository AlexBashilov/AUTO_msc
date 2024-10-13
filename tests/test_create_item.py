import pytest
import uuid
from internal.api_utils.api_utils import ApiClient
from internal.post_create_item import post_create_items
from internal.models.responseModels import RequestCreateItems
from internal.connection import create_connection, execute_read_query



class TestCreateItems:
    @pytest.fixture(scope='class')
    def client(self):
        return ApiClient()
    
    def test_create_item(self, client):
        body = RequestCreateItems(
            item_name=str('fantomas6'),
            guid=str(uuid.uuid4()),
            description=str('opisanie')
        )
        response = post_create_items(client, body)
        print(client)
        assert response.status_code == 201


def test_get_only_one_new_item():
    connection = create_connection(
    "booker","root" , "root", "127.0.0.1","5433"
    )
    select_users = "SELECT guid FROM book_cost_items WHERE guid = '04758184-78c7-455f-91ac-dcb169b9350c'"
    users = execute_read_query(connection, select_users)
    connection.close()
    assert '04758184-78c7-455f-91ac-dcb169b9350c' in str(users)

def test_delete_item():
    pass
