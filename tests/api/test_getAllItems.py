#import uuid
from http import HTTPStatus
import utils.api_utils as api_utils
from api_pages import routes
from api_pages.models import getAllItems, GetItemsByID
from api_pages.models.GetItemsByID import GetOneItemsByIDResponseSchema, GetOneItemsByIDDetailsResponse
from data_base.models.Items_db import ItemsDB
from data_base.db_queries import SqlQueries

class TestGetAllItems:
    # def test_get_all_items(self,client, db_connection):
    #     db = SqlQueries(db_connection)
    #     get_all = SqlQueries.get_all_items(self)
    #     print(get_all)
    #     response = api_utils.get_request(client, routes.Routes.GET_ALL_ITEMS)
    #     print(response)
    #     api_utils.assert_response_code(HTTPStatus.OK, response.status_code)
        #api_utils.assert_schema(response, getAllItems.GetAllItemsResponseSchema)
        # Сходить в БД и сделать селект всех строк.
        # Пробежаться в цикле по GetAllItemsResponseSchema внутри по массиву, и сверить что массив из БД совпадает с массивом из ответа(Response)

    def test_get_items_by_id(self,client, db_connection):
        db = SqlQueries(db_connection)
        new_items = ItemsDB.generate_random_item()
        insert_item = db.insert_new_item(new_items)
        expected_response = GetOneItemsByIDResponseSchema(
            details="success",
            result=GetOneItemsByIDDetailsResponse(insert_item,new_items.item_name,new_items.guid,new_items.description)
        )
        response = api_utils.get_request(client, routes.Routes.GET_ONE_ITEM+str(insert_item))
        api_utils.assert_response_data(expected_response, response )
        print(expected_response)
        print(insert_item)
        # Написали тест для получения одного итема. пока с ошибкой
        
        
        # get_one_item = SqlQueries.get_items_by_id(self,)
        # print(get_one_item)
        # api_utils.assert_response_code(HTTPStatus.OK, response.status_code)
        