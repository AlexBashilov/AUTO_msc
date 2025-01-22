#import uuid
from http import HTTPStatus
import utils.api_utils as api_utils
from api_pages import routes
from api_pages.models import getAllItems, GetItemsByID
from api_pages.models.GetItemsByID import GetOneItemsByIDResponseSchema, GetOneItemsByIDDetailsResponse, \
    GetOneItemParams
from data_base.models.Items_db import ItemsDB
from data_base.db_queries import SqlQueries

class TestGetAllItems:
    # def test_get_all_items(self,client, db_connection):
        # db = SqlQueries(db_connection)
        # get_all = SqlQueries.get_all_items(db)
        # print(get_all)
        # response = api_utils.get_request(client, routes.Routes.GET_ALL_ITEMS)
        # print(response.json())
        # api_utils.assert_response_code(HTTPStatus.OK, response.status_code)
        # api_utils.assert_schema(response, getAllItems.GetAllItemsResponseSchema) #ответ из БД не совпадает с ответом гет запроса
        # Сходить в БД и сделать селект всех строк.
        # Пробежаться в цикле по GetAllItemsResponseSchema внутри по массиву, и сверить что массив из БД совпадает с массивом из ответа(Response)

    def test_get_items_by_id(self,client, db_connection):
        db = SqlQueries(db_connection)
        new_items = ItemsDB.generate_random_item()
        insert_item = db.insert_new_item(new_items)
        response_by_one = api_utils.get_request(client, routes.Routes.GET_ONE_ITEM + str(insert_item))
        expected_response = GetOneItemsByIDResponseSchema(
            result='success',
            details=GetOneItemsByIDDetailsResponse(id=insert_item) #выдает ошибку что нужно 3 поля, а мы по все 3 поля передаем лишь id
        )
        response_by_one = api_utils.get_request(client, routes.Routes.GET_ONE_ITEM+str(insert_item))
        api_utils.assert_response_code(HTTPStatus.OK, response_by_one.status_code)
        api_utils.assert_response_data(expected_response, response_by_one )
        print(expected_response)
        print(insert_item)
        # Написали тест для получения одного итема. пока с ошибкой
        
        
        # get_one_item = SqlQueries.get_items_by_id(self,)
        # print(get_one_item)
        # api_utils.assert_response_code(HTTPStatus.OK, response.status_code)
        