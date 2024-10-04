from dataclasses import dataclass


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