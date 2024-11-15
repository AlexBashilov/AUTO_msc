from dataclasses import dataclass


@dataclass
class Drivers:
    LAST_NAME: str = "Фамилия"
    FIRST_NAME: str = "Имя"
    MIDDLE_NAME: str = "Отчество"
    PHONE_NUMBER: str = "Номер телефона"
    PASSPORT_NUMBER: str = "Серия номер паспорта"
    PASSPORT_DATE: str = "Когда выдан"
    LICENSE_NUMBER: str = "Водительское удостоверение"
