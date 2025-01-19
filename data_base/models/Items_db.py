from dataclasses import dataclass
#import datetime
import time
import uuid

#import allure
from faker import Faker


@dataclass
class ItemsDB:
    id: int
    item_name: str
    guid: str
    description: str
    deleted_at: time

    @staticmethod
    #@allure.step("Сгенерировать данные для добавления нового водителя в БД")
    def generate_random_item():
        fake = Faker("ru_RU")

        return ItemsDB(
            item_name=fake.last_name(),
            guid=uuid.uuid4(),
            description=fake.word(),
        )
