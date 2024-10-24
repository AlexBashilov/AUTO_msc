import enum


class ErrorTransportCompaniesMessages(enum.StrEnum):
    """
    Ошибки при создании транспортных компаний
    """
    KPP_BLANK = 'Ошибка валидации запроса: Kpp: cannot be blank.'
    OGRN_BLANK = 'Ошибка валидации запроса: Ogrn: cannot be blank.'
    INN_BLANK = 'Ошибка валидации запроса: Inn: cannot be blank.'
    CONTRACT_DATE_BLANK = ('parsing body body from "" failed, because parsing time "" as "2006-01-02": cannot parse "" '
                           'as "2006"')
    CONTRACT_NUMBER_BLANK = 'Ошибка валидации запроса: ContractNumber: cannot be blank.'
    CONTACT_FACE_TRANSPORTER_BLANK = 'Ошибка валидации запроса: FullName: cannot be blank.'
    POSITION_OF_CONTACT_PERSON_BLANK = 'Ошибка валидации запроса: Position: cannot be blank.'
    OWNERSHIP_FORM_BLANK = 'body.params.ownership_form_id in body is required'
    FULL_NAME_OF_THE_TRANSPORTER_BLANK = 'body.params.fullName in body is required'
    REGISTERED_ADDRESS_TRANSPORTER_BLANK = 'body.params.legalAddress in body is required'
