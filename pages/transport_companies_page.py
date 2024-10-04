import allure
from helperpackage import HelperWd
from testData.transport_companies import TransportCompanies


class TransportCompaniesPage:
    TRANSPORT_COMPANY_FILTER = '#select-companyName-filter'
    FILTER_TK = '#select-companyName-filter input'
    CREATE_BUTTON = '#createBtn'
    SAVE_BUTTON = '[data-qa="btn-save"]'
    ACCEPT_BUTTON = '[data-qa="button-accept"]'

    def __init__(self, driver):
        self.helper = HelperWd(driver)

    @allure.step('Проверить наименование активных элементов на странице')
    def check_transport_companies_page_elements(self):
        assert self.helper.wait_for_element_visible('h2').text == 'Транспортные компании'
        assert self.helper.wait_for_element_visible('[data-qa=active-switch]').text == 'Только с активными шаблонами'
        assert self.helper.wait_for_element_visible('#clearFilters').text == 'Очистить фильтры'
        assert self.helper.wait_for_element_visible(self.CREATE_BUTTON).text == 'Добавить ТК'
        self.helper.wait_for_element_visible(self.TRANSPORT_COMPANY_FILTER)

    @allure.step('Нажать на кнопку "Создать ТК"')
    def create_transport_company(self):
        self.helper.wait_for_element_visible(self.CREATE_BUTTON).click()
        self.helper.wait_for_element_visible(self.SAVE_BUTTON)

    @allure.step('Заполнить данные по ТК')
    def fill_transport_company(self, tkInfo):
        if TransportCompanies.FULL_NAME_OF_THE_TRANSPORTER in tkInfo:
            self.helper.fill_field(
                '[data-qa="tk-full-name"] input',
                tkInfo[TransportCompanies.FULL_NAME_OF_THE_TRANSPORTER])

        if TransportCompanies.REGISTERED_ADDRESS_TRANSPORTER in tkInfo:
            self.helper.fill_field(
                '[data-qa="tk-legal-address"] input',
                tkInfo[TransportCompanies.REGISTERED_ADDRESS_TRANSPORTER])

        if TransportCompanies.SHORT_NAME_TRANSPORTER in tkInfo:
            self.helper.fill_field(
                '[data-qa="tk-short-name"] input',
                tkInfo[TransportCompanies.SHORT_NAME_TRANSPORTER])

        if TransportCompanies.OWNERSHIP_FORM in tkInfo:
            self.helper.wait_for_element_visible('[data-qa="tk-ownership-form-id"]').click()
            self.helper.wait_for_element_visible(
                '//span[text()="' + tkInfo[TransportCompanies.OWNERSHIP_FORM] + '"]').click()

        if TransportCompanies.OGRN_TRANSPORTER in tkInfo:
            self.helper.fill_field(
                '[data-qa="tk-ogrn"] input',
                tkInfo[TransportCompanies.OGRN_TRANSPORTER])

        if TransportCompanies.KPP_TRANSPORTER in tkInfo:
            self.helper.fill_field(
                '[data-qa="tk-kpp"] input',
                tkInfo[TransportCompanies.KPP_TRANSPORTER])

        if TransportCompanies.INN_TRANSPORTER in tkInfo:
            self.helper.fill_field(
                '[data-qa="tk-inn"] input',
                tkInfo[TransportCompanies.INN_TRANSPORTER])

        if TransportCompanies.CONTRACT_NUMBER in tkInfo:
            self.helper.fill_field(
                '[data-qa="tk-contract-number"] input',
                tkInfo[TransportCompanies.CONTRACT_NUMBER])

        if TransportCompanies.CONTRACT_DATE in tkInfo:
            self.helper.wait_for_element_visible('[data-qa="tk-contract-date"]').click()
            self.helper.fill_field(
                '[data-qa="tk-contract-date"] input',
                tkInfo[TransportCompanies.CONTRACT_DATE])

        if TransportCompanies.CONTACT_FACE_TRANSPORTER in tkInfo:
            self.helper.fill_field(
                '[data-qa="tk-contact-person-full-name"] input',
                tkInfo[TransportCompanies.CONTACT_FACE_TRANSPORTER])

        if TransportCompanies.POSITION_OF_CONTACT_PERSON in tkInfo:
            self.helper.fill_field(
                '[data-qa="tk-position"] input',
                tkInfo[TransportCompanies.POSITION_OF_CONTACT_PERSON])

        if TransportCompanies.PHONE_NUMBER in tkInfo:
            self.helper.fill_field(
                '[data-qa="tk-phone-number"] input',
                tkInfo[TransportCompanies.PHONE_NUMBER])

    @allure.step('Нажать на кнопку "Сохранить" при создании транспортной компании')
    def save_transport_company(self):
        self.helper.wait_for_element_visible(self.SAVE_BUTTON).click()
        self.helper.wait_for_element_invisibility(self.SAVE_BUTTON)

    @allure.step('Найти ТК по фильтру')
    def filter_transport_company(self, tkInfo):
        self.helper.wait_for_element_visible(self.TRANSPORT_COMPANY_FILTER).click()
        self.helper.wait_for_element_visible(self.FILTER_TK)
        self.helper.fill_field_with_delay(self.FILTER_TK, tkInfo[TransportCompanies.SHORT_NAME_TRANSPORTER])
        self.helper.wait_for_element_visible(
            '//span[text()="' + tkInfo[TransportCompanies.SHORT_NAME_TRANSPORTER] + '"]').click()

    @allure.step('Удалить первую ТК в списке')
    def delete_first_transport_company_on_the_list(self, tkInfo):
        self.helper.wait_for_element_visible('[data-qa^="action-delete-modal"]').click()
        self.helper.wait_for_element_visible(self.ACCEPT_BUTTON)
        assert (tkInfo[TransportCompanies.SHORT_NAME_TRANSPORTER] in
                self.helper.wait_for_element_visible('[data-qa="typo-delete-tc"]').text), \
            'Сообщение при удалении не содержит краткое имя ТК!'
        self.helper.wait_for_element_visible(self.ACCEPT_BUTTON).click()
        self.helper.wait_for_element_invisibility(self.ACCEPT_BUTTON)

    @allure.step('Проверить что на странице нет указанной ТК')
    def check_lack_transport_company_on_the_list(self, tkInfo):
        self.helper.wait_for_element_visible(self.TRANSPORT_COMPANY_FILTER).click()
        self.helper.wait_for_element_visible(self.FILTER_TK)
        self.helper.fill_field_with_delay(self.FILTER_TK, tkInfo[TransportCompanies.SHORT_NAME_TRANSPORTER])
        self.helper.wait_for_element_invisibility('//span[text()="' + tkInfo[TransportCompanies.SHORT_NAME_TRANSPORTER] + '"]')

    @allure.step('Перейти в первую ТК в списке')
    def go_to_first_transport_company_on_the_list(self):
        self.helper.wait_for_element_visible('[href^="/transport-companies"]').click()

    @allure.step('Проверить ошибку при создании транспортной компании')
    def check_error_message_after_save_transport_company(self, expectedError):
        self.helper.wait_for_element_visible(self.SAVE_BUTTON).click()
        assert self.helper.wait_for_element_visible(
            '[data-qa^="error-message"]').text == expectedError, 'Сообщение об ошибке не совпадает!'
