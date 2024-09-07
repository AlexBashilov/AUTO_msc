import allure
from helperpackage import HelperWd


class TransportCompaniesPage:
    TRANSPORT_COMPANY_FILTER = '#select-companyName-filter'
    CREATE_BUTTON = '#createBtn'

    def __init__(self, driver):
        self.helper = HelperWd(driver)

    @allure.step('Проверить наименование активных элементов на странице')
    def check_transport_companies_page_elements(self):
        assert self.helper.wait_for_element_visible('h2').text == 'Транспортные компании'
        assert self.helper.wait_for_element_visible('[data-qa=active-switch]').text == 'Только с активными шаблонами'
        assert self.helper.wait_for_element_visible('#clearFilters').text == 'Очистить фильтры'
        assert self.helper.wait_for_element_visible(self.CREATE_BUTTON).text == 'Добавить ТК'
        self.helper.wait_for_element_visible(self.TRANSPORT_COMPANY_FILTER)
