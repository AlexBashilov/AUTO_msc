from dataclasses import dataclass
from faker import Faker


@dataclass
class TransportCompanies:
    FULL_NAME_OF_THE_TRANSPORTER = 'Полное наименование перевозчика'
    REGISTERED_ADDRESS_TRANSPORTER = 'Юридический адрес ТК'
    SHORT_NAME_TRANSPORTER = 'Краткое наименование перевозчика'
    OWNERSHIP_FORM = 'Форма собственности'
    OWNERSHIP_FORM_TYPE_OOO = 'ООО'
    OWNERSHIP_FORM_TYPE_OAO = 'ОАО'
    OWNERSHIP_FORM_TYPE_ZAO = 'ЗАО'
    OWNERSHIP_FORM_TYPE_AO = 'АО'
    OWNERSHIP_FORM_TYPE_IP = 'ИП'
    OGRN_TRANSPORTER = 'ОГРН ТК'
    KPP_TRANSPORTER = 'КПП ТК'
    INN_TRANSPORTER = 'ИНН ТК'
    CONTRACT_NUMBER = 'Номер договора'
    CONTRACT_DATE = 'Дата договора'
    CONTACT_FACE_TRANSPORTER = 'ФИО контактного лица'
    POSITION_OF_CONTACT_PERSON = 'Должность'
    PHONE_NUMBER = 'Номер телефона'
    EMAIL = 'Почта контактного лица'

    def generate_random_tc(self, case_name, faker):
        tc = {
            self.FULL_NAME_OF_THE_TRANSPORTER: 'ТК для кейса ' + case_name + str(faker.random_number(digits=3)),
            self.REGISTERED_ADDRESS_TRANSPORTER: faker.address(),
            self.SHORT_NAME_TRANSPORTER: 'ТК для кейса ' + str(faker.random_number(digits=3)),
            self.OWNERSHIP_FORM: self.OWNERSHIP_FORM_TYPE_OOO,
            self.OGRN_TRANSPORTER: faker.random_number(digits=15),
            self.KPP_TRANSPORTER: faker.random_number(digits=9, fix_len=True),
            self.INN_TRANSPORTER: faker.random_number(digits=12),
            self.CONTRACT_NUMBER: faker.random_number(digits=20),
            # self.CONTRACT_DATE: fake.date(pattern='%d-%m-%Y'),
            self.CONTRACT_DATE: '09012024',
            self.CONTACT_FACE_TRANSPORTER: faker.name(),
            self.POSITION_OF_CONTACT_PERSON: faker.job(),
            self.PHONE_NUMBER: faker.phone_number(),
            self.EMAIL: faker.email()
        }
        return tc
