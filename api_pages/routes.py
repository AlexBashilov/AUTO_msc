from enum import Enum


class Routes(str, Enum):
    """
    Все REST ручки
    """

    GET_ALL_ITEMS = "/book_cost_items/get_all"
    GET_ONE_ITEM = "/book_cost_items/get_only_one/"
    CREATE_COST_ITEM = "/book_cost_items/create"
    DELETE_COST_ITEM = "/book_cost_items/delete/"
    UPDATE_COST_ITEM = "/book_cost_items/update/"

    def __str__(self) -> str:
        return self.value
