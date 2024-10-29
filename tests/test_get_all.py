import requests
from decouple import config
# from internal.api_utils.api_utils import ApiClient
# from internal.post_create_item import post_create_items
# from internal.models.responseModels import RequestCreateItems
from internal.connection import create_connection, execute_read_query


URL_GetAll = config('LOCALHOST_Get_All')


def get_all_items_from_db():
    connection = create_connection(
    "booker","root" , "root", "127.0.0.1","5433"
    )
    select_users = 'SELECT "items"."id", "items"."item_name", "items"."guid", "items"."description", "items"."deleted_at"  FROM "book_cost_items" AS "items" WHERE (deleted_at is null)'
    users = execute_read_query(connection, select_users)
    print(users)
    connection.close()

def test_get_all():
    res = requests.get(URL_GetAll)
    assert res.status_code == 200
    # assert res.json(object_pairs_hook=list[tuple]) == get_all_items_from_db()
    print(res.json(object_pairs_hook=list[tuple]))

test_get_all()
get_all_items_from_db()