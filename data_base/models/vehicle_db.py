from dataclasses import dataclass
import datetime

import allure
from faker import Faker


@dataclass
class VehicleDB:
    vehicle_type_id: int
    number: str
    brand: int
    model: str
    vehicle_ownership_type_id: int
    capacity_type_id: int
    capacity_volume: int
    cargo_body_type_id: int
    weight_capacity: float
    created_at: datetime
    updated_at: datetime
    id: int = None

    @staticmethod
    @allure.step("Сгенерировать данные для добавления нового ТС в БД")
    def generate_random_vehicle():
        fake = Faker("ru_RU")

        return VehicleDB(
            vehicle_type_id=fake.random_int(1, 3),
            number=fake.bothify("?###??##").upper(),
            brand=fake.random_int(1, 50),
            model="Автотест",
            vehicle_ownership_type_id=fake.random_int(1, 4),
            capacity_type_id=fake.random_int(1, 10),
            capacity_volume=fake.random_int(1, 100),
            cargo_body_type_id=fake.random_int(1, 19),
            weight_capacity=fake.pyfloat(min_value=1, max_value=50),
            created_at=datetime.date.today(),
            updated_at=datetime.date.today(),
        )
