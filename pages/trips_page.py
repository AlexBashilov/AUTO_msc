import allure
from helperpackage import HelperWd


class TripsPage:

    def __init__(self, driver):
        self.helper = HelperWd(driver)

    @allure.step('Проверить наименование активных элементов на странице')
    def check_trips_page_elements(self):
        assert self.helper.wait_for_element_visible('h2').text == 'Рейсы'
        self.helper.wait_for_element_visible('//span[text()="Время, от"]')
        self.helper.wait_for_element_visible('//span[text()="Дата первой точки"]')
        self.helper.wait_for_element_visible('//span[text()="Время, до"]')
        self.helper.wait_for_element_visible('//span//span[text()="Id рейса"]')
        self.helper.wait_for_element_visible('//span[text()="Статус рейса"]')
        self.helper.wait_for_element_visible('//span//span[text()="Тип рейса"]')
        self.helper.wait_for_element_visible('//span[text()="Название ТК"]')
        self.helper.wait_for_element_visible('//span[text()="Номер ТС"]')
        self.helper.wait_for_element_visible('//span//span[text()="Водитель"]')
        self.helper.wait_for_element_visible('//span[text()=" Сбросить фильтры "]')
        self.helper.wait_for_element_visible('//span[text()=" Скачать дашборд "]')
