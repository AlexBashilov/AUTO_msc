from test_data.drivers import Drivers
from test_data.error_drivers_messages import ErrorDriversMessages
from faker import Faker


class InvalidDrivers:
    def list_of_invalid_drivers_parameters(self):
        fake = Faker('ru_RU')
        return [
            {
                'name': 'Создание водителя без имени',
                'allureID': '39703',
                Drivers.LAST_NAME: fake.last_name(),
                Drivers.MIDDLE_NAME: fake.middle_name(),
                Drivers.PHONE_NUMBER: fake.bothify('9#########'),
                Drivers.PASSPORT_NUMBER: fake.passport_number(),
                Drivers.PASSPORT_DATE: '01012000',
                Drivers.LICENSE_NUMBER: fake.random_number(digits=10),
            },
            {
                'name': 'Создание водителя без фамилии',
                'allureID': '39702',
                Drivers.FIRST_NAME: fake.first_name(),
                Drivers.MIDDLE_NAME: fake.middle_name(),
                Drivers.PHONE_NUMBER: fake.bothify('9#########'),
                Drivers.PASSPORT_NUMBER: fake.passport_number(),
                Drivers.PASSPORT_DATE: '01012000',
                Drivers.LICENSE_NUMBER: fake.random_number(digits=10),
            },
            {
                'name': 'Создание водителя без номера телефона',
                'allureID': '39704',
                Drivers.LAST_NAME: fake.last_name(),
                Drivers.FIRST_NAME: fake.first_name(),
                Drivers.MIDDLE_NAME: fake.middle_name(),
                Drivers.PASSPORT_NUMBER: fake.passport_number(),
                Drivers.PASSPORT_DATE: '01012000',
                Drivers.LICENSE_NUMBER: fake.random_number(digits=10),
            },
            {
                'name': 'Создание водителя без серии и номера паспорта',
                'allureID': '39705',
                Drivers.LAST_NAME: fake.last_name(),
                Drivers.FIRST_NAME: fake.first_name(),
                Drivers.MIDDLE_NAME: fake.middle_name(),
                Drivers.PHONE_NUMBER: fake.bothify('9#########'),
                Drivers.PASSPORT_DATE: '01012000',
                Drivers.LICENSE_NUMBER: fake.random_number(digits=10),
            },
            {
                'name': 'Создание водителя без даты выдачи паспорта',
                'allureID': '39706',
                Drivers.LAST_NAME: fake.last_name(),
                Drivers.FIRST_NAME: fake.first_name(),
                Drivers.MIDDLE_NAME: fake.middle_name(),
                Drivers.PHONE_NUMBER: fake.bothify('9#########'),
                Drivers.PASSPORT_NUMBER: fake.passport_number(),
                Drivers.LICENSE_NUMBER: fake.random_number(digits=10),
            },
            {
                'name': 'Создание водителя без ВУ',
                'allureID': '41044',
                Drivers.LAST_NAME: fake.last_name(),
                Drivers.FIRST_NAME: fake.first_name(),
                Drivers.MIDDLE_NAME: fake.middle_name(),
                Drivers.PHONE_NUMBER: fake.bothify('9#########'),
                Drivers.PASSPORT_NUMBER: fake.passport_number(),
                Drivers.PASSPORT_DATE: '01012000',
            }, ]

    def list_of_same_drivers_parameters(self):
        fake = Faker('ru_RU')
        return [
            {
                'name': 'Создание водителя с тем же номером паспорта, что уже существует в системе',
                'allureID': '37489',
                Drivers.FIRST_NAME: fake.first_name(),
                Drivers.LAST_NAME: fake.last_name(),
                Drivers.MIDDLE_NAME: fake.middle_name(),
                Drivers.PHONE_NUMBER: fake.bothify('9#########'),
                Drivers.PASSPORT_NUMBER: fake.passport_number(),
                Drivers.PASSPORT_DATE: '01012000',
                Drivers.LICENSE_NUMBER: fake.random_number(digits=10),
                'error': ErrorDriversMessages.SAME_PASSPORT_ERROR
            },
        ]
