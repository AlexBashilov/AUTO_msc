from datetime import datetime

from allure_commons._allure import step
from pydantic import BaseModel

from utils.base_utils import none_to_empty_string, combined_dict_with_list, clean_and_transform_string


@step("Сравнить отправленные данные в запросе на ручку createDriver с данными в БД")
def create_driver_validation_data(request_model: BaseModel, db_driver_data, db_driver_tc):
    assert len(db_driver_data) == 1, 'В таблице driver должна быть ровно 1 запись!'
    driver_db_data = db_driver_data[0]
    driver_tc = combined_dict_with_list(db_driver_tc)
    assert request_model.params.transportCompanyIds == driver_tc['transport_company_id']
    assert request_model.params.surname == driver_db_data['surname'], 'Фамилия водителя не совпадает!'
    assert none_to_empty_string(request_model.params.patronymic) == driver_db_data['patronymic'], 'Отчество водителя не совпадает!'
    assert request_model.params.name == driver_db_data['name'], 'Имя водителя не совпадает!'
    assert request_model.params.phoneNumber == driver_db_data['phone_number'], 'Телефон водителя не совпадает!'
    assert request_model.params.passportDate == str(driver_db_data['passport_date']), 'Дата действия паспорта водителя не совпадает!'
    assert clean_and_transform_string(request_model.params.passportFullNumber) == driver_db_data['passport_full_number'], 'Номер паспорта водителя не совпадает!'
    assert request_model.params.licenseNumber == driver_db_data['license_number'], 'Номер ВУ водителя не совпадает!'
    assert 1 == driver_db_data['state'], 'Статус водителя не совпадает!'
    assert datetime.now().strftime("%Y-%m-%d") == str(driver_db_data['created_at']), 'Дата создания водителя не совпадает!'