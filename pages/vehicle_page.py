import allure
from helperpackage import HelperWd
from testData.vehicles import Vehicles


class VehiclePage:
    SAVE_BUTTON = '[data-qa="btn-save"]'
    ACCEPT_BUTTON = '[data-qa="button-accept"]'
    CREATE_VEHICLE_BUTTON = '[data-qa="btn-add-transport"]'
    VEHICLE_NUMBER_FILTER = 'input[data-qa="filter-vehicle-number"]'
    OK_BUTTON_WHERE_INSPECT_VEHICLE = '[data-qa="btn-ok"]'
    SELECT_EXISTING_VEHICLE_BUTTON = '[data-qa="btn-select-existing-vehicle"]'

    def __init__(self, driver):
        self.helper = HelperWd(driver)

    @allure.step('Нажать на кнопку "Добавить ТС"')
    def create_vehicle(self):
        self.helper.wait_for_element_visible(self.CREATE_VEHICLE_BUTTON, 15).click()
        self.helper.wait_for_element_visible(self.SAVE_BUTTON, 15)

    @allure.step('Заполнить поля для создания транспортного средства')
    def fill_vehicle(self, vehicleInfo):
        self.helper.wait_for_element_visible(self.SAVE_BUTTON, 15)

        if Vehicles.TYPE_VEHICLE in vehicleInfo:
            self.helper.wait_for_element_visible('[data-qa="form-vehicle-type"]').click()
            self.helper.wait_for_element_visible('//*[@data-qa="form-vehicle-type"]//span[text()="' + vehicleInfo[Vehicles.TYPE_VEHICLE] + '"]').click()

        if Vehicles.MARK_VEHICLE in vehicleInfo:
            self.helper.wait_for_element_visible('[data-qa="form-vehicle-brand"]').click()
            self.helper.wait_for_element_visible('//span[text()="' + vehicleInfo[Vehicles.MARK_VEHICLE] + '"]').click()

        if Vehicles.MODEL_VEHICLE in vehicleInfo:
            self.helper.fill_field(
                'input[data-qa="form-vehicle-model"]',
                vehicleInfo[Vehicles.MODEL_VEHICLE]
            )

        if Vehicles.PALLET_CAPACITY in vehicleInfo:
            self.helper.wait_for_element_visible('[data-qa="form-capacity"]').click()
            self.helper.wait_for_element_visible('//*[@data-qa="form-capacity"]//span[text()="' + vehicleInfo[Vehicles.PALLET_CAPACITY] + '"]').click()

        if Vehicles.CAPACITY_CENTIMETERS in vehicleInfo:
            self.helper.fill_field(
                'input[data-qa="form-capacity-square"]',
                vehicleInfo[Vehicles.CAPACITY_CENTIMETERS]
            )

        if Vehicles.BODY_TYPE in vehicleInfo:
            self.helper.wait_for_element_visible('[data-qa="form-cargo-body-type"]').click()
            self.helper.wait_for_element_visible('//span[text()="' + vehicleInfo[Vehicles.BODY_TYPE] + '"]').click()

        if Vehicles.NUMBER in vehicleInfo:
            self.helper.fill_field(
                'input[data-qa="form-vehicle-number"]',
                vehicleInfo[Vehicles.NUMBER]
            )

        if Vehicles.PAYLOAD in vehicleInfo:
            self.helper.fill_field(
                'input[data-qa="form-weight-capacity"]',
                vehicleInfo[Vehicles.PAYLOAD]
            )

    @allure.step('Нажать на кнопку "Сохранить" при создании транспортного средства')
    def save_vehicle(self):
        self.helper.wait_for_element_visible(self.SAVE_BUTTON).click()
        self.helper.wait_for_element_invisibility(self.SAVE_BUTTON)

    @allure.step('Найти транспортное средство по фильтру')
    def filter_vehicle(self, vehicleInfo):
        self.helper.wait_for_element_visible(self.VEHICLE_NUMBER_FILTER)
        self.helper.fill_field(
            self.VEHICLE_NUMBER_FILTER,
            vehicleInfo[Vehicles.NUMBER]
        )
        self.helper.wait_for_element_visible('//span[text()="' + vehicleInfo[Vehicles.NUMBER] + '"]')

    @allure.step('Удалить первое транспортное средство в списке')
    def delete_first_vehicle_on_the_list(self, vehicleInfo):
        self.helper.wait_for_element_visible('[data-qa^="action-delete-vehicle"]', 15).click()
        self.helper.wait_for_element_visible(self.ACCEPT_BUTTON, 15)
        assert (vehicleInfo[Vehicles.NUMBER] in self.helper.wait_for_element_visible('[data-qa="typo-delete-vehicle"]').text), \
            'Сообщение при удалении не содержит номер ТС!'
        self.helper.wait_for_element_visible(self.ACCEPT_BUTTON, 15).click()
        self.helper.wait_for_element_invisibility(self.ACCEPT_BUTTON, 15)

    @allure.step('Проверить что на странице нет указанного транспортного средства')
    def check_lack_vehicle_on_the_list(self, vehicleInfo):
        self.helper.wait_for_element_visible(self.VEHICLE_NUMBER_FILTER, 15)
        self.helper.fill_field_with_delay(
            self.VEHICLE_NUMBER_FILTER,
            vehicleInfo[Vehicles.NUMBER]
        )
        self.helper.wait_for_element_invisibility('//span[text()="' + vehicleInfo[Vehicles.NUMBER] + '"]')

    @allure.step('Проверить ошибку при создании транспортного средства')
    def check_error_message_after_save_vehicle(self, expectedError):
        self.helper.wait_for_element_visible(self.SAVE_BUTTON).click()
        assert (expectedError in self.helper.wait_for_element_visible('[class^="_error"]').text), \
            'Сообщение об ошибке не совпадает!'

    @allure.step('Нажать на кнопку "Выбрать уже имеющееся ТС" при создании транспортного средства и выбрать ТС по гос. номеру')
    def select_existing_vehicle(self, vehicleInfo):
        self.helper.wait_for_element_visible(self.SELECT_EXISTING_VEHICLE_BUTTON, 15).click()
        self.helper.wait_for_element_invisibility(self.SELECT_EXISTING_VEHICLE_BUTTON, 15)
        self.helper.wait_for_element_visible('[data-qa="existing-vehicle-select"]', 15).click()
        self.helper.fill_field_with_delay(
            '[data-qa="existing-vehicle-select"] input',
            vehicleInfo[Vehicles.NUMBER],
        )
        self.helper.wait_for_element_visible('//span[text()="' + vehicleInfo[Vehicles.NUMBER] + '"]', 15).click()
        self.helper.wait_for_element_visible('//*[@data-qa="form-vehicle-type"]//span[text()="' + vehicleInfo[Vehicles.TYPE_VEHICLE] + '"]', 15)
        self.helper.wait_for_element_visible('//*[@data-qa="existing-vehicle-select"]//span[text()="' + vehicleInfo[Vehicles.NUMBER] + '"]', 15)

    @allure.step('Нажать на кнопку "Глаз" для просмотра ТС')
    def click_on_vehicle_view(self):
        self.helper.wait_for_element_visible('[data-qa^="action-open-vehicle"]', 15).click()
        self.helper.wait_for_element_visible(self.OK_BUTTON_WHERE_INSPECT_VEHICLE, 15)

    @allure.step('Проверить наличие примечания о принадлежности ТС к другим ТК и его текст')
    def check_note_existing_vehicle(self):
        self.helper.wait_for_element_visible(self.OK_BUTTON_WHERE_INSPECT_VEHICLE, 15)
        assert ('ТС также числится в других ТК' in self.helper.wait_for_element_visible('[data-qa="note-vehicle-in-another"]').text), \
            'Нет примечания о принадлежности ТС к другим ТК!'
        self.helper.wait_for_element_visible(self.OK_BUTTON_WHERE_INSPECT_VEHICLE, 15).click()
