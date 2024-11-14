from dataclasses import dataclass
import datetime

import allure
from faker import Faker


@dataclass
class DriversDB:
    surname: str
    name: str
    patronymic: str
    phone_number: str
    passport_full_number: str
    passport_date: datetime
    state: int
    created_at: datetime
    license_number: str
    id: int = None

    @staticmethod
    @allure.step("Сгенерировать данные для добавления нового водителя в БД")
    def generate_random_driver():
        fake = Faker("ru_RU")

        return DriversDB(
            surname=fake.last_name(),
            name=fake.first_name(),
            patronymic=fake.middle_name(),
            phone_number=fake.bothify("9#########"),
            passport_full_number=fake.passport_number(),
            passport_date=datetime.date.today(),
            state=1,
            created_at=datetime.date.today(),
            license_number=str(fake.random_number(digits=10)),
        )
