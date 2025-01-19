#import uuid
from http import HTTPStatus
import utils.api_utils as api_utils
from api_pages import routes
from api_pages.models import getAllItems
#from data_base.models.Items_db import ItemDB
from data_base.db_queries import SqlQueries


class TestGetAllItems:
    def test_get_all_items(self,client, db_connection):
        db = SqlQueries(db_connection)
        
        response = api_utils.get_request(client, routes.Routes.GET_ALL_ITEMS)
        print(response)
        api_utils.assert_response_code(HTTPStatus.OK, response.status_code)
        #api_utils.assert_schema(response, getAllItems.GetAllItemsResponseSchema)
