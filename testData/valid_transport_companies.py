from testData.transport_companies import TransportCompanies
from faker import Faker


class ValidTransportCompanies:
    def list_of_transport_companies_parameters(self):
        fake = Faker('ru_RU')

        return [
            {
                'name': 'Создание транспортной компании тип владения "ООО" и её последующее удаление',
                'allureID': '27651',
                TransportCompanies.FULL_NAME_OF_THE_TRANSPORTER: 'Автотестовая ТК тип владения "ООО"',
                TransportCompanies.REGISTERED_ADDRESS_TRANSPORTER: fake.address(),
                TransportCompanies.SHORT_NAME_TRANSPORTER: 'Авто Регресс №' + str(fake.random_number(digits=3)),
                TransportCompanies.OWNERSHIP_FORM: TransportCompanies.OWNERSHIP_FORM_TYPE_OOO,
                TransportCompanies.OGRN_TRANSPORTER: fake.random_number(digits=15),
                TransportCompanies.KPP_TRANSPORTER: fake.random_number(digits=9, fix_len=True),
                TransportCompanies.INN_TRANSPORTER: fake.random_number(digits=12),
                TransportCompanies.CONTRACT_NUMBER: fake.random_number(digits=20),
                TransportCompanies.CONTRACT_DATE: '09012024',
                TransportCompanies.CONTACT_FACE_TRANSPORTER: fake.name(),
                TransportCompanies.POSITION_OF_CONTACT_PERSON: fake.job(),
                TransportCompanies.PHONE_NUMBER: fake.phone_number(),
                TransportCompanies.EMAIL: fake.email()
            },
            {
                'name': 'Создание транспортной компании тип владения "ЗАО" и её последующее удаление ',
                'allureID': '54541',
                TransportCompanies.FULL_NAME_OF_THE_TRANSPORTER: 'Автотестовая транспортная компания Регресс 2',
                TransportCompanies.REGISTERED_ADDRESS_TRANSPORTER: fake.address(),
                TransportCompanies.SHORT_NAME_TRANSPORTER: 'Авто Регресс №' + str(fake.random_number(digits=3)),
                TransportCompanies.OWNERSHIP_FORM: TransportCompanies.OWNERSHIP_FORM_TYPE_ZAO,
                TransportCompanies.OGRN_TRANSPORTER: fake.random_number(digits=15),
                TransportCompanies.KPP_TRANSPORTER: fake.random_number(digits=9, fix_len=True),
                TransportCompanies.INN_TRANSPORTER: fake.random_number(digits=12),
                TransportCompanies.CONTRACT_NUMBER: fake.random_number(digits=20),
                TransportCompanies.CONTRACT_DATE: '09012024',
                TransportCompanies.CONTACT_FACE_TRANSPORTER: fake.name(),
                TransportCompanies.POSITION_OF_CONTACT_PERSON: fake.job(),
                TransportCompanies.PHONE_NUMBER: fake.phone_number(),
                TransportCompanies.EMAIL: fake.email()
            },
            {
                'name': 'Создание транспортной компании тип владения "ИП" и её последующее удаление ',
                'allureID': '54542',
                TransportCompanies.FULL_NAME_OF_THE_TRANSPORTER: 'Автотестовая транспортная компания Регресс 3',
                TransportCompanies.REGISTERED_ADDRESS_TRANSPORTER: fake.address(),
                TransportCompanies.SHORT_NAME_TRANSPORTER: 'Авто Регресс №' + str(fake.random_number(digits=3)),
                TransportCompanies.OWNERSHIP_FORM: TransportCompanies.OWNERSHIP_FORM_TYPE_IP,
                TransportCompanies.OGRN_TRANSPORTER: fake.random_number(digits=15),
                TransportCompanies.KPP_TRANSPORTER: fake.random_number(digits=9, fix_len=True),
                TransportCompanies.INN_TRANSPORTER: fake.random_number(digits=12),
                TransportCompanies.CONTRACT_NUMBER: fake.random_number(digits=20),
                TransportCompanies.CONTRACT_DATE: '09012024',
                TransportCompanies.CONTACT_FACE_TRANSPORTER: fake.name(),
                TransportCompanies.POSITION_OF_CONTACT_PERSON: fake.job(),
                TransportCompanies.PHONE_NUMBER: fake.phone_number(),
                TransportCompanies.EMAIL: fake.email()
            },
            {
                'name': 'Создание транспортной компании тип владения "ИП" без КПП',
                'allureID': '54543',
                TransportCompanies.FULL_NAME_OF_THE_TRANSPORTER: 'Автотестовая транспортная компания Регресс 4',
                TransportCompanies.REGISTERED_ADDRESS_TRANSPORTER: fake.address(),
                TransportCompanies.SHORT_NAME_TRANSPORTER: 'Авто Регресс №' + str(fake.random_number(digits=3)),
                TransportCompanies.OWNERSHIP_FORM: TransportCompanies.OWNERSHIP_FORM_TYPE_IP,
                TransportCompanies.OGRN_TRANSPORTER: fake.random_number(digits=15),
                TransportCompanies.INN_TRANSPORTER: fake.random_number(digits=12),
                TransportCompanies.CONTRACT_NUMBER: fake.random_number(digits=20),
                TransportCompanies.CONTRACT_DATE: '09012024',
                TransportCompanies.CONTACT_FACE_TRANSPORTER: fake.name(),
                TransportCompanies.POSITION_OF_CONTACT_PERSON: fake.job(),
                TransportCompanies.PHONE_NUMBER: fake.phone_number(),
                TransportCompanies.EMAIL: fake.email()
            },
            {
                'name': 'Создание транспортной компании тип владения "ОАО" и её последующее удаление ',
                'allureID': '54544',
                TransportCompanies.FULL_NAME_OF_THE_TRANSPORTER: 'Автотестовая транспортная компания Регресс 5',
                TransportCompanies.REGISTERED_ADDRESS_TRANSPORTER: fake.address(),
                TransportCompanies.SHORT_NAME_TRANSPORTER: 'Авто Регресс №' + str(fake.random_number(digits=3)),
                TransportCompanies.OWNERSHIP_FORM: TransportCompanies.OWNERSHIP_FORM_TYPE_OAO,
                TransportCompanies.OGRN_TRANSPORTER: fake.random_number(digits=15),
                TransportCompanies.KPP_TRANSPORTER: fake.random_number(digits=9, fix_len=True),
                TransportCompanies.INN_TRANSPORTER: fake.random_number(digits=12),
                TransportCompanies.CONTRACT_NUMBER: fake.random_number(digits=20),
                TransportCompanies.CONTRACT_DATE: '09012024',
                TransportCompanies.CONTACT_FACE_TRANSPORTER: fake.name(),
                TransportCompanies.POSITION_OF_CONTACT_PERSON: fake.job(),
                TransportCompanies.PHONE_NUMBER: fake.phone_number(),
                TransportCompanies.EMAIL: fake.email()
            },
            {
                'name': 'Создание транспортной компании тип владения "АО" и её последующее удаление ',
                'allureID': '54545',
                TransportCompanies.FULL_NAME_OF_THE_TRANSPORTER: 'Автотестовая транспортная компания Регресс 6',
                TransportCompanies.REGISTERED_ADDRESS_TRANSPORTER: fake.address(),
                TransportCompanies.SHORT_NAME_TRANSPORTER: 'Авто Регресс №' + str(fake.random_number(digits=3)),
                TransportCompanies.OWNERSHIP_FORM: TransportCompanies.OWNERSHIP_FORM_TYPE_AO,
                TransportCompanies.OGRN_TRANSPORTER: fake.random_number(digits=15),
                TransportCompanies.KPP_TRANSPORTER: fake.random_number(digits=9, fix_len=True),
                TransportCompanies.INN_TRANSPORTER: fake.random_number(digits=12),
                TransportCompanies.CONTRACT_NUMBER: fake.random_number(digits=20),
                TransportCompanies.CONTRACT_DATE: '09012024',
                TransportCompanies.CONTACT_FACE_TRANSPORTER: fake.name(),
                TransportCompanies.POSITION_OF_CONTACT_PERSON: fake.job(),
                TransportCompanies.PHONE_NUMBER: fake.phone_number(),
                TransportCompanies.EMAIL: fake.email()
            }]
