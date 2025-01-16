from typing import List

from api_pages.models import createDriver
from faker import Faker

from test_data.api.error_create_driver import CreateDriverError


def create_valid_drivers_parameters() -> List[dict]:
    fake = Faker("ru_RU")
    return [
        {
            "name": "Создание водителя с валидными данными",
            "allureID": "65759",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
        },
        {
            "name": "Создание водителя без отчества",
            "allureID": "41034",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
        },
        {
            "name": "Создания водителя с несколькими ТК",
            "allureID": "37465",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39, 41],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
        },
        {
            "name": "Создания водителя с паспортом в 20 символов",
            "allureID": "65765",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=str(fake.random_number(digits=20)),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
        },
        {
            "name": "Проверка приведение номера паспорта к определенному виду",
            "allureID": "38032",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.bothify(
                        text=" ????!@*&#### ", letters="йцукенфывапasdfghQW"
                    ),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
        },
    ]


def create_drivers_required_parameters() -> List[dict]:
    fake = Faker("ru_RU")
    return [
        {
            "name": "Создания водителя без ТК",
            "allureID": "37466",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.TC_ID_REQUIRED_ERROR,
        },
        {
            "name": "Создания водителя без фамилии",
            "allureID": "65778",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.SURNAME_REQUIRED_ERROR,
        },
        {
            "name": "Создания водителя без имени",
            "allureID": "65779",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.NAME_REQUIRED_ERROR,
        },
        {
            "name": "Создания водителя без номера телефона",
            "allureID": "65780",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.PHONE_NUMBER_REQUIRED_ERROR,
        },
        {
            "name": "Создания водителя без номера паспорта",
            "allureID": "65781",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.PASSPORT_FULL_NUMBER_REQUIRED_ERROR,
        },
        {
            "name": "Создания водителя без даты действия паспорта",
            "allureID": "65782",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.PASSPORT_DATE_REQUIRED_ERROR,
        },
        {
            "name": "Создание водителя без ВУ",
            "allureID": "41035",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                )
            ),
            "expected_error": CreateDriverError.LICENSE_NUMBER_REQUIRED_ERROR,
        },
    ]


def create_drivers_errors() -> List[dict]:
    fake = Faker("ru_RU")
    return [
        {
            "name": "Создания водителя с пустыми ТК",
            "allureID": "65788",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.EMPTY_TC_ID_ERROR,
        },
        {
            "name": "Создания водителя с пустой фамилией",
            "allureID": "65789",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname="",
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.EMPTY_SURNAME_ERROR,
        },
        {
            "name": "Создания водителя с пустым именем",
            "allureID": "65790",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name="",
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.EMPTY_NAME_ERROR,
        },
        {
            "name": "Создания водителя с пустым номером телефона",
            "allureID": "65791",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber="",
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.EMPTY_PHONE_NUMBER_ERROR,
        },
        {
            "name": "Создания водителя с пустым номером паспорта",
            "allureID": "65792",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber="",
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.EMPTY_PASSPORT_NUMBER_ERROR,
        },
        {
            "name": "Создания водителя с пустым ВУ",
            "allureID": "65782",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=fake.passport_number(),
                    passportDate=fake.date(),
                    licenseNumber="",
                )
            ),
            "expected_error": CreateDriverError.EMPTY_LICENSE_NUMBER_ERROR,
        },
        {
            "name": "Создания водителя с паспортом > 20 символов",
            "allureID": "65793",
            "request_body": createDriver.CreateDriverRequestSchema(
                params=createDriver.CreateDriverRequestParams(
                    transportCompanyIds=[39],
                    surname=fake.last_name(),
                    name=fake.first_name(),
                    patronymic=fake.middle_name(),
                    phoneNumber=fake.bothify("9#########"),
                    passportFullNumber=str(fake.random_number(digits=21)),
                    passportDate=fake.date(),
                    licenseNumber=str(fake.random_number(digits=10)),
                )
            ),
            "expected_error": CreateDriverError.PASSPORT_LENGTH_ERROR,
        },
    ]
