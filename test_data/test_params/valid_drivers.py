from test_data.drivers import Drivers
from faker import Faker


class ValidDrivers:
    def list_of_drivers_parameters(self):
        fake = Faker('ru_RU')
        return [
            {
                'name': 'Создание водителя с валидными данными',
                'allureID': '37490',
                Drivers.LAST_NAME: fake.last_name(),
                Drivers.FIRST_NAME: fake.first_name(),
                Drivers.MIDDLE_NAME: fake.middle_name(),
                Drivers.PHONE_NUMBER: fake.bothify('9#########'),
                Drivers.PASSPORT_NUMBER: fake.passport_number(),
                Drivers.PASSPORT_DATE: '01012000',
                Drivers.LICENSE_NUMBER: fake.random_number(digits=10),
            },
            {
                'name': 'Создание водителя без отчества',
                'allureID': '41045',
                Drivers.LAST_NAME: fake.last_name(),
                Drivers.FIRST_NAME: fake.first_name(),
                Drivers.PHONE_NUMBER: fake.bothify('9#########'),
                Drivers.PASSPORT_NUMBER: fake.passport_number(),
                Drivers.PASSPORT_DATE: '01012000',
                Drivers.LICENSE_NUMBER: fake.random_number(digits=10),
            }
        ]
