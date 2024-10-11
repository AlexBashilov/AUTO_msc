from enum import Enum


class Routes(str, Enum):
    createItemsRoute = 'book_cost_items/create'
    
    def __str__(self) -> str:
        return self.value
