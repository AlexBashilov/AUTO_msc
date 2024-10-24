import allure
from helperpackage import HelperWd
from test_data.drivers import Drivers


class DriversPage:
    SAVE_BUTTON = '[data-qa="btn-save"]'
    CREATE_BUTTON = '#createBtn'
    DRIVERS_TAB = '//span[text()="Водители"]'
    DRIVER_PHONE_NUMBER_FILTER = '[data-qa="filter-phone-number"]'
    DRIVER_PHONE_NUMBER_FILTER_INPUT = '[data-qa="filter-phone-number"] input'
    TABLE_DATA = '//tbody'
    ACCEPT_BUTTON = '[data-qa="button-accept"]'

    def __init__(self, driver):
        self.helper = HelperWd(driver)

    @allure.step('Перейти во вкладку водители на странице ТК')
    def goToDriversTab(self):
        self.helper.wait_for_element_visible(self.DRIVERS_TAB, 15).click()
        self.helper.wait_for_element_visible(self.DRIVER_PHONE_NUMBER_FILTER, 15)

    @allure.step('Нажать на кнопку "Добавить водителя"')
    def createDriver(self):
        self.helper.wait_for_element_visible(self.CREATE_BUTTON, 15).click()
        self.helper.wait_for_element_visible(self.SAVE_BUTTON, 15)

    @allure.step('Заполнить поля для создания водителя')
    def fillDriver(self, driverInfo):
        self.helper.wait_for_element_visible(self.SAVE_BUTTON, 15)

        if Drivers.LAST_NAME in driverInfo:
            self.helper.fill_field(
                'input[data-qa="form-surname"]',
                driverInfo[Drivers.LAST_NAME]
            )

        if Drivers.FIRST_NAME in driverInfo:
            self.helper.fill_field(
                'input[data-qa="form-name"]',
                driverInfo[Drivers.FIRST_NAME]
            )

        if Drivers.MIDDLE_NAME in driverInfo:
            self.helper.fill_field(
                'input[data-qa="form-patronymic"]',
                driverInfo[Drivers.MIDDLE_NAME]
            )

        if Drivers.PHONE_NUMBER in driverInfo:
            self.helper.fill_field(
                'input[data-qa="form-phone"]',
                driverInfo[Drivers.PHONE_NUMBER]
            )

        if Drivers.PASSPORT_NUMBER in driverInfo:
            self.helper.fill_field(
                'input[data-qa="form-passport-number"]',
                driverInfo[Drivers.PASSPORT_NUMBER]
            )

        if Drivers.PASSPORT_DATE in driverInfo:
            self.helper.fill_field(
                'input[data-qa="form-passport-date"]',
                driverInfo[Drivers.PASSPORT_DATE]
            )

        if Drivers.LICENSE_NUMBER in driverInfo:
            self.helper.fill_field(
                'input[data-qa="form-license-number"]',
                driverInfo[Drivers.LICENSE_NUMBER]
            )

    @allure.step('Нажать на кнопку "Сохранить" при создании водителя')
    def saveDriver(self):
        self.helper.wait_for_element_visible(self.SAVE_BUTTON, 15).click()
        self.helper.wait_for_element_invisibility(self.SAVE_BUTTON, 15)

    @allure.step('Проверить что кнопка "Сохранить" при создании водителя заблокирована')
    def checkDisableSaveDriverButton(self):
        self.helper.wait_for_element_visible('[data-qa="btn-save"][disabled=""]')

    @allure.step('Проверить ошибку при создании водителя')
    def checkErrorMessageAfterSaveDriver(self, expectedError):
        self.helper.wait_for_element_visible(self.SAVE_BUTTON).click()
        assert self.helper.wait_for_element_visible('[data-qa^="error-message"]').text == expectedError, \
            'Сообщение об ошибке не совпадает!'

    @allure.step('Найти водителя по фильтру номера телефона')
    def filterDriverByPhoneNumber(self, driverInfo):
        self.helper.wait_for_element_visible(self.DRIVER_PHONE_NUMBER_FILTER).click()
        self.helper.wait_for_element_visible(self.DRIVER_PHONE_NUMBER_FILTER_INPUT)
        self.helper.fill_field_with_delay(
            self.DRIVER_PHONE_NUMBER_FILTER_INPUT,
            driverInfo[Drivers.PHONE_NUMBER],
        )
        self.helper.wait_for_element_visible('//span[text()="+7' + driverInfo[Drivers.PHONE_NUMBER] + '"]').click()
        assert ('+7' + driverInfo[Drivers.PHONE_NUMBER]) in self.helper.wait_for_element_visible(self.TABLE_DATA).text, \
            'Табличная часть водителей не содержит номер телефона водителя!'
        self.helper.wait_for_element_visible('//span[text()="+7' + driverInfo[Drivers.PHONE_NUMBER] + '"]').click()

    @allure.step('Удалить первого водителя в списке')
    def deleteFirstDriverOnTheList(self, driverInfo):
        if Drivers.MIDDLE_NAME in driverInfo:
            fioDriver = driverInfo[Drivers.LAST_NAME] + ' ' + driverInfo[Drivers.FIRST_NAME] + ' ' + driverInfo[
                Drivers.MIDDLE_NAME]
        else:
            fioDriver = driverInfo[Drivers.LAST_NAME] + ' ' + driverInfo[Drivers.FIRST_NAME]
        self.helper.wait_for_element_visible('[data-qa^="action-delete-driver"]', 15).click()
        self.helper.wait_for_element_visible(self.ACCEPT_BUTTON)
        self.helper.wait_for_element_invisibility('//*[contains(text(),"undefined")]', 15)
        assert fioDriver in self.helper.wait_for_element_visible('[data-qa="typo-delete-driver"]').text, 'Сообщение при удалении не содержит ФИО водителя!'
        self.helper.wait_for_element_visible(self.ACCEPT_BUTTON, 15).click()
        self.helper.wait_for_element_invisibility(self.ACCEPT_BUTTON, 15)

    @allure.step('Проверить что на странице нет указанного водителя по номеру телефона')
    def checkLackDriverOnTheList(self, driverInfo):
        self.helper.wait_for_element_visible(self.DRIVER_PHONE_NUMBER_FILTER, 15).click()
        self.helper.wait_for_element_visible(self.DRIVER_PHONE_NUMBER_FILTER_INPUT)
        self.helper.fill_field_with_delay(
            self.DRIVER_PHONE_NUMBER_FILTER_INPUT,
            driverInfo[Drivers.PHONE_NUMBER],
        )
        self.helper.wait_for_element_invisibility('//span[text()="+7' + driverInfo[Drivers.PHONE_NUMBER] + '"]')
