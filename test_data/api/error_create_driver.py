import enum


class CreateDriverError(enum.StrEnum):
    """
    Ошибки при создании водителей в ручке createDriver
    """

    TC_ID_REQUIRED_ERROR = "body.params.transportCompanyIds in body is required"
    SURNAME_REQUIRED_ERROR = "body.params.surname in body is required"
    NAME_REQUIRED_ERROR = "body.params.name in body is required"
    PHONE_NUMBER_REQUIRED_ERROR = "body.params.phoneNumber in body is required"
    PASSPORT_DATE_REQUIRED_ERROR = "body.params.passportDate in body is required"
    PASSPORT_FULL_NUMBER_REQUIRED_ERROR = "body.params.passportFullNumber in body is required"
    LICENSE_NUMBER_REQUIRED_ERROR = "body.params.licenseNumber in body is required"
    EMPTY_TC_ID_ERROR = "Ошибка валидации запроса: массив TransportCompanyIDs не должен быть пустым"
    EMPTY_SURNAME_ERROR = "Ошибка валидации запроса: поле Surname должно быть не пустое"
    EMPTY_NAME_ERROR = "Ошибка валидации запроса: поле Name должно быть не пустое"
    EMPTY_PHONE_NUMBER_ERROR = "Ошибка валидации запроса: поле PhoneNumber должно быть не пустое"
    EMPTY_PASSPORT_NUMBER_ERROR = (
        "Ошибка валидации запроса: поле PassportFullNumber должно быть не пустое"
    )
    EMPTY_LICENSE_NUMBER_ERROR = (
        'Ошибка создания водителя: Необходимо заполнить поле "Водительское удостоверение"'
    )
    PASSPORT_LENGTH_ERROR = (
        "Ошибка валидации запроса: паспорт не должен включать больше 20 символов"
    )
    SAME_PASSPORT_ERROR = (
        "Ошибка создания водителя: Водитель с таким номером паспорта уже существует"
    )
