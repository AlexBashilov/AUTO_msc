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

    def generate_random_tc(self, case_name) -> dict:
        fake = Faker('ru_RU')

        tc = {
            self.FULL_NAME_OF_THE_TRANSPORTER: 'ТК для кейса ' + case_name,
            self.REGISTERED_ADDRESS_TRANSPORTER: fake.address(),
            self.SHORT_NAME_TRANSPORTER: 'ТК для кейса №' + str(fake.random_number(digits=3)),
            self.OWNERSHIP_FORM: self.OWNERSHIP_FORM_TYPE_OOO,
            self.OGRN_TRANSPORTER: fake.random_number(digits=15),
            self.KPP_TRANSPORTER: fake.random_number(digits=9, fix_len=True),
            self.INN_TRANSPORTER: fake.random_number(digits=12, fix_len=True),
            self.CONTRACT_NUMBER: fake.random_number(digits=20),
            self.CONTRACT_DATE: '09012024',  # Дату не фейкую, потому что поле куда вводим почему-то не всегда стабильно работает, а вот с этой датой, всегда стабильно
            self.CONTACT_FACE_TRANSPORTER: fake.name(),
            self.POSITION_OF_CONTACT_PERSON: fake.job(),
            self.PHONE_NUMBER: fake.phone_number(),
            self.EMAIL: fake.email()
        }
        return tc
