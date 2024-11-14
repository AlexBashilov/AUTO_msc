import allure
from helperpackage import HelperWd


class Route:
    CREATE_BUTTON = "#createBtn"
    SAVE_ROUTE_BUTTON = "#upsertRouteBtn"
    DISABLE_SAVE_ROUTE_BUTTON = '//button[@id="upsertRouteBtn"][@disabled=""]'
    FIRST_POINT_FILTER = "#firstPointFilter"
    LAST_POINT_FILTER = "#lastPointFilter"
    ANY_POINT_FILTER = "#anyPointFilter"
    ROUTE_NAME_FILTER = "#routeNameFilter"
    TOOLTIP_LABEL = '[data-qa="note-wrapper"]'
    ADD_OPERATION_BUTTON = "#startAddingOperationBtn"
    POINT_NAME_SELECT = "#pointName"
    POINT_NAME_INPUT = "#pointName input"
    OPERATION_NAME_SELECT = "#selectedOperation"

    def __init__(self, driver):
        self.helper = HelperWd(driver)

    @allure.step("Проверить наименование активных элементов на странице")
    def check_route_page_elements(self):
        assert self.helper.wait_for_element_visible("h2").text == "Маршруты"
        self.helper.wait_for_element_visible('[data-qa="active-switch"]')
        assert (
            self.helper.wait_for_element_visible('[data-qa="active-switch"]').text
            == "Маршруты с шаблонами"
        )
        assert (
            self.helper.wait_for_element_visible("#clearFilters").text
            == "Очистить фильтры"
        )
        assert (
            self.helper.wait_for_element_visible(self.CREATE_BUTTON).text
            == "Создать новый маршрут"
        )
        assert (
            self.helper.wait_for_element_visible(self.FIRST_POINT_FILTER).text
            == "Поиск по первой точке"
        )
        assert (
            self.helper.wait_for_element_visible("#anyPointFilter").text
            == "Поиск по любой точке"
        )
        assert (
            self.helper.wait_for_element_visible(self.LAST_POINT_FILTER).text
            == "Поиск по последней точке"
        )
        assert (
            self.helper.wait_for_element_visible("#routeNameFilter").text
            == "Поиск по названию маршрута"
        )

    @allure.step('Нажать на кнопку "Создать маршрут"')
    def create_route(self):
        self.helper.wait_for_element_visible(self.CREATE_BUTTON).click()
        self.helper.wait_for_element_visible(self.DISABLE_SAVE_ROUTE_BUTTON)
        assert (
            self.helper.wait_for_element_visible(self.TOOLTIP_LABEL).text
            == 'Значения в колонке "Разгрузка из" будут сбрасываться, после каждого изменения. Внести значения '
            "необходимо перед сохранением маршрута"
        ), "Текст тултипа не совпадает!"

    @allure.step('Нажать на кнопку "Создать на основании" у первого маршрута')
    def create_route_based_on(self):
        self.helper.wait_for_element_visible('[data-qa="create-on-based"]').click()
        # Добавил тут вейт, потому что дальше не отрабатывает удаление... Оно видит иконку и
        # кликает по ней, но операция не удаляется, я не смог понять почему
        self.helper.wait_(1)
        self.helper.wait_for_element_visible('//button[@id="upsertRouteBtn"]')
        assert (
            self.helper.wait_for_element_visible(self.TOOLTIP_LABEL).text
            == 'Значения в колонке "Разгрузка из" будут сбрасываться, после каждого изменения. Внести '
            "значения необходимо перед сохранением маршрута"
        ), "Текст тултипа не совпадает!"
