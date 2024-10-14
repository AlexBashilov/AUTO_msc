from dataclasses import dataclass


@dataclass
class ErrorDriversMessages:
    SAME_PASSPORT_ERROR = 'Ошибка создания водителя: Водитель с таким номером паспорта уже существует'
    SAME_DRIVER_LICENCE_ERROR = 'Ошибка создания водителя: Водитель с таким удостоверением уже есть'
