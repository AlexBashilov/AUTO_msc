from datetime import datetime
from typing import List

from allure import step
from helperpackage import HelperWd

from data_base.db_queries import SqlQueries
from test_data.route_filter import RouteFilter


class RoutePage:
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

    @step("Проверить наименование активных элементов на странице")
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

    @step('Нажать на кнопку "Создать маршрут"')
    def create_route(self):
        self.helper.wait_for_element_visible(self.CREATE_BUTTON).click()
        self.helper.wait_for_element_visible(self.DISABLE_SAVE_ROUTE_BUTTON)
        assert (
            self.helper.wait_for_element_visible(self.TOOLTIP_LABEL).text
            == 'Значения в колонке "Разгрузка из" будут сбрасываться, после каждого изменения. Внести значения '
            "необходимо перед сохранением маршрута"
        ), "Текст тултипа не совпадает!"

    @step('Нажать на кнопку "Создать на основании" у первого маршрута')
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

    @step("Установить федеральный округ {1} в маршруте")
    def set_federal_district(self, federal_district):
        self.helper.wait_for_element_visible('[data-qa="federalDistrict"]').click()
        self.helper.fill_field('[data-qa="federalDistrict"] input', federal_district)
        self.helper.wait_for_element_visible(
            f'//div[@data-qa="federalDistrict"]//span[text()="{federal_district}"]'
        ).click()

    @step("Добавить операцию в маршрут. Название точки - {1} Операция - {2}.")
    def add_operation_in_route(self, route_point, operation_type, unload_point=None):
        if self.helper.check_element_on_page(self.ADD_OPERATION_BUTTON):
            self.helper.wait_for_element_visible(self.ADD_OPERATION_BUTTON).click()
        self.helper.wait_for_element_visible(self.POINT_NAME_SELECT).click()
        self.helper.fill_field_with_delay(self.POINT_NAME_INPUT, route_point)
        self.helper.wait_for_element_visible(
            f'//div[@id="pointName"]//span[text()="{route_point}"]'
        ).click()

        self.helper.wait_for_element_visible(self.OPERATION_NAME_SELECT).click()
        self.helper.wait_for_element_visible(
            f'//div[@id="selectedOperation"]//span[text()="{operation_type}"]'
        ).click()

        self.helper.wait_for_element_visible("#addOperationBtn").click()
        self.helper.wait_for_element_visible(
            f'//div[@data-qa="table-route-operations"]//td//span[text()="{route_point}"]'
        )
        self.helper.wait_for_element_visible(
            f'//div[@data-qa="table-route-operations"]//td//span[text()="{operation_type}"]'
        )

        if unload_point:
            self.helper.wait_for_element_visible(
                f'//td//span[text()="{route_point}"]//..//..//div[@id="relatedOperation"]'
            ).click()
            self.helper.wait_for_element_visible(
                f'//td//span[text()="{route_point}"]//..//..//div[@id="relatedOperation"]//div[text()[contains(.,"{unload_point}")]]'
            ).click()

    @step('Нажать на кнопку "Сохранить маршрут"')
    def save_route(self):
        self.helper.wait_for_element_visible(self.SAVE_ROUTE_BUTTON).click()
        self.helper.wait_for_element_invisibility(self.SAVE_ROUTE_BUTTON, 45)

    @step('Проверить что кнопка "Сохранить маршрут" заблокирована')
    def check_lock_save_button(self):
        self.helper.wait_for_element_visible(self.DISABLE_SAVE_ROUTE_BUTTON)

    @step("Проверить ошибку при сохранении маршрута")
    def check_error_message_after_save_route(self, expected_error):
        error_text = "#errorMessage0"

        self.helper.wait_for_element_visible(self.SAVE_ROUTE_BUTTON).click()
        self.helper.wait_for_element_visible(error_text)
        assert (
            expected_error in self.helper.wait_for_element_visible(error_text).text
        ), "Сообщение об ошибке не совпадает!"

    @step("Отфильтровать маршруты по первой точке маршрута")
    def filtering_routes_by_first_points(self, first_route_point):
        self.helper.wait_for_element_visible(self.FIRST_POINT_FILTER).click()
        self.helper.fill_field("#firstPointFilter input", first_route_point)
        self.helper.wait_for_element_visible(
            f'//div[@id="firstPointFilter"]//span[text()="{first_route_point}"]'
        ).click()

    @step("Проверить что маршруты отфильтровались по фильтру {1}")
    def check_filtering_routes(self, filter, filter_point):
        self.helper.wait_for_element_visible('//*[@id="routesTable"]//td[1]')
        row_count = len(self.helper.grab_multiple('//*[@id="routesTable"]//tbody//tr'))
        for i in range(row_count):
            filtering_route_name = self.helper.wait_for_element(
                f'//*[@id="routesTable"]//tr[{i}]//td[3]'
            ).text
            filtering_route_points = filtering_route_name.split(" >> ")
            match filter:
                case RouteFilter.FIRST_POINT_FILTER:
                    assert (
                        filtering_route_points[0] == filter_point
                    ), "Первая точка маршрута не совпадает"

                case RouteFilter.ANY_POINT_FILTER:
                    assert (
                        filtering_route_name == filter_point
                    ), "Точка не содержится в маршруте"

                case RouteFilter.LAST_POINT_FILTER:
                    assert (
                        filtering_route_points[-1] == filter_point
                    ), "Последняя точка маршрута не совпадает"
                case RouteFilter.ROUTE_NAME_FILTER:
                    assert (
                        filtering_route_name == filter_point
                    ), "Название маршрута не совпадает"

    @step("Отфильтровать маршруты по последней точке маршрута")
    def filtering_routes_by_last_points(self, last_route_point):
        self.helper.wait_for_element_visible(self.LAST_POINT_FILTER).click()
        self.helper.fill_field("#lastPointFilter input", last_route_point)
        self.helper.wait_for_element_visible(
            f'//div[@id="lastPointFilter"]//span[text()="{last_route_point}"]'
        ).click()

    @step("Отфильтровать маршруты по любой точке маршрута")
    def filtering_routes_by_any_points(self, any_route_point):
        self.helper.wait_for_element_visible(self.ANY_POINT_FILTER).click()
        self.helper.fill_field("#anyPointFilter input", any_route_point)
        self.helper.wait_for_element_visible(
            f'//div[@id="anyPointFilter"]//span[text()="{any_route_point}"]'
        ).click()

    @step("Отфильтровать маршруты по названию маршрута")
    def filtering_routes_by_route_name(self, route_name):
        self.helper.wait_for_element_visible(self.ROUTE_NAME_FILTER).click()
        self.helper.fill_field_with_delay("#routeNameFilter input", route_name, 0.01)
        self.helper.wait_for_element_visible(
            f'//div[@id="routeNameFilter"]//span[text()="{route_name}"]', 60
        ).click()

    @step("Получить полное название маршрута")
    def get_full_route_name(self, route_points: List[dict]) -> str:
        route_name = ""

        if len(route_points) < 2:
            assert False, "Маршрут состоит менее чем из двух точек!"
        for i in range(len(route_points)):
            if i == (len(route_points) - 1):
                route_name = route_name + route_points[i]["pointName"]
            else:
                route_name = route_name + route_points[i]["pointName"] + " >> "
        return route_name

    @step('Изменить состояние фильтра "Маршруты с активными шаблонами" на {1}')
    def filtering_routes_by_activity(self, is_enable):
        toggle_class = self.helper.grab_attribute(
            '[data-qa="active-switch"] label', "class"
        )
        current_state = "active" in toggle_class
        if current_state != is_enable:
            self.helper.wait_for_element_visible(
                '[data-qa="active-switch"] label'
            ).click()

    @step('Нажать на кнопку "Очистить фильтр" и проверить что фильтры очистились')
    def clear_route_filter(self):
        self.helper.wait_for_element_visible("#clearFilters").click()
        assert self.helper.wait_for_element(
            '(//div[@id="firstPointFilter"]//span)[4]'
        ).text, 'Фильтр "Поиск по первой точке" не очищен'
        assert self.helper.wait_for_element(
            '(//div[@id="anyPointFilter"]//span)[4]'
        ).text, 'Фильтр "Поиск по любой точке" не очищен'
        assert self.helper.wait_for_element(
            '(//div[@id="lastPointFilter"]//span)[4]'
        ).text, 'Фильтр "Поиск по последней точке" не очищен'
        assert self.helper.wait_for_element(
            '(//div[@id="routeNameFilter"]//span)[4]'
        ).text, 'Фильтр "Поиск по названию маршрута" не очищен'
        self.helper.wait_for_element_visible('//*[@id="routesTable"]//td[1]')
        row_count = len(self.helper.grab_multiple('//*[@id="routesTable"]//tbody//tr'))
        assert row_count < 2, "В выдаче менее 2ух рейсов! Фильтры не очистились"

    @step("Проверить корректное отображение созданного маршрута")
    def check_created_route(self, user_name, route_name, route_district):
        today = datetime.now().strftime("%d.%m.%Y")
        self.filtering_routes_by_route_name(route_name)
        self.helper.wait_for_element_visible('//*[@id="routesTable"]//td[1]')

        assert (
            self.helper.wait_for_element('//*[@id="routesTable"]//td[2]').text == today
        ), "Дата создания маршрута не совпадает!"
        assert (
            self.helper.wait_for_element('//*[@id="routesTable"]//td[3]').text
            == route_name
        ), "Наименование маршрута не совпадает!"
        assert (
            self.helper.wait_for_element('//*[@id="routesTable"]//td[4]').text
            == route_district
        ), "Федеральный округ созданного рейса отличается!"
        assert (
            self.helper.wait_for_element('//*[@id="routesTable"]//td[5]').text == "Нет"
        ), "У созданного рейса есть активные шаблоны!"
        assert (
            self.helper.wait_for_element('//*[@id="routesTable"]//td[6]').text
            == user_name
        ), "Имя пользователя, создавшего рейс, не совпадает!"

    @step("Проверить что маршруты не отображаются")
    def check_empty_route(self):
        self.helper.wait_for_element_invisibility('//*[@id="routesTable"]//td[1]')

    @step("Удалить первый маршрут в списке")
    def delete_first_route(self):
        modal_window = '[data-qa="modal-delete-route"]'

        self.helper.wait_for_element_visible("#deleteBtn").click()
        self.helper.wait_for_element_visible(modal_window)
        self.helper.wait_for_element_visible('[data-qa="button-accept"]').click()
        self.helper.wait_for_element_invisibility(modal_window, 30)
        self.helper.wait_for_element_invisibility('//*[@id="routesTable"]//td[1]', 30)

    @step("Закрыть окно с созданием маршрута")
    def close_create_route_window(self):
        self.helper.wait_for_element_visible('[data-qa="modal-route-create"] a').click()
        self.helper.wait_for_element_invisibility('[data-qa="modal-route-create"]', 30)

    @step("Проверить что нельзя добавить операцию разгрузки первой строкой")
    def check_lock_unload_operation(self, route_point, operation_type):
        if self.helper.check_element_on_page(self.ADD_OPERATION_BUTTON):
            self.helper.wait_for_element_visible(self.ADD_OPERATION_BUTTON).click()
        self.helper.wait_for_element_visible(self.POINT_NAME_SELECT).click()
        self.helper.fill_field(self.POINT_NAME_INPUT, route_point)
        self.helper.wait_for_element_visible(
            f'//div[@id="pointName"]//span[text()="{route_point}"]'
        ).click()
        self.helper.wait_for_element_visible(self.OPERATION_NAME_SELECT).click()
        self.helper.wait_for_element_visible(
            f'//div[@id="selectedOperation"]//span[text()="{operation_type}"]/parent::div[@class[contains(.,"disabled")]]'
        )
        self.helper.wait_for_element_visible(self.DISABLE_SAVE_ROUTE_BUTTON)

    @step(
        "Проверить операции у открытого на редактирование/созданного на основании маршрута"
    )
    def check_open_route(self, route_point_operations):
        for i in range(len(route_point_operations)):
            assert self.helper.wait_for_element_visible(
                f'//div[@data-qa="table-route-operations"]//tbody//tr[{i + 1}]//td[1]//span',
                2,
            ).text == str(i + 1), "Номер операции не совпадает!"
            assert (
                self.helper.wait_for_element_visible(
                    f'//div[@data-qa="table-route-operations"]//tbody//tr[{i + 1}]//td[2]//span',
                    2,
                ).text
                == route_point_operations[i]["pointName"]
            ), "Название точки не совпадает!"
            assert (
                self.helper.wait_for_element_visible(
                    f'//div[@data-qa="table-route-operations"]//tbody//tr[{i + 1}]//td[3]//span',
                    2,
                ).text
                == route_point_operations[i]["operationType"]
            ), "Тип операции не совпадает!"
            if route_point_operations[i]["unloadPoint"]:
                assert (
                    route_point_operations[i]["unloadPoint"]
                    in self.helper.wait_for_element_visible(
                        f'//div[@data-qa="table-route-operations"]//tbody//tr[{i + 1}]//td[4]//div//div//span[2]',
                        2,
                    ).text
                ), "Точка разгрузки не совпадает!"

    @step("Удалить операцию из маршрута по её номеру")
    def delete_operation_in_route_by_number(self, number_of_operation):
        self.helper.wait_for_element_visible(
            f'//div[@data-qa="table-route-operations"]//tbody//tr[{number_of_operation}]//td[7]//button'
        ).click()

    @step("Удалить маршрут из БД по точкам если по маршруту не было рейсов")
    def delete_route_from_db_by_points(self, db_connection, route_name):
        db = SqlQueries(db_connection)
        route_points = route_name.split(" >> ")
        count_trips = db.get_trips_by_route_name(route_name)
        count_routes = db.get_routes_by_route_name(route_name)

        if count_routes != 0:
            if count_trips == 0:
                route_id = db.get_route_data_by_route_name(route_name)[0][0]
                for k in range(len(route_points)):
                    route_pont_id = db.get_route_point_by_route_id(route_id)
                    db.delete_route_operation_by_route_point_id(route_pont_id)
                    db.delete_route_point_by_route_point_id(route_pont_id)
                db.delete_route_point_by_route_id(route_id)
                db.delete_route_by_route_name(route_name)
                assert True, "Маршрут удален из БД"
            else:
                assert False, "По маршруту были созданы рейсы, нельзя удалять!"
        else:
            assert True, "Маршрут не создан, удаление из БД не требуется"
