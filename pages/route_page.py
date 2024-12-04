from datetime import datetime
from typing import List

from allure import step
from helperpackage import HelperWd

from data_base.db_queries import SqlQueries
from test_data.route_filter import RouteFilter


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

    @step('Установить федеральный округ {1} в маршруте')
    def setFederalDistrict(self, federalDistrict):
        self.helper.wait_for_element_visible('[data-qa="federalDistrict"]').click()
        self.helper.fill_field('[data-qa="federalDistrict"] input', federalDistrict)
        self.helper.wait_for_element_visible(f'//div[@data-qa="federalDistrict"]//span[text()="{federalDistrict}"]').click()

    @step('Добавить операцию в маршрут. Название точки - {1} Операция - {2}.')
    def addOperationInRoute(self, routePoint, operationType, unloadPoint = None):
        if self.helper.check_element_on_page(self.ADD_OPERATION_BUTTON):
            self.helper.wait_for_element_visible(self.ADD_OPERATION_BUTTON).click()
        self.helper.wait_for_element_visible(self.POINT_NAME_SELECT).click()
        self.helper.fill_field(self.POINT_NAME_INPUT, routePoint)
        self.helper.wait_for_element_visible(f'//div[@id="pointName"]//span[text()="{routePoint}"]').click()

        self.helper.wait_for_element_visible(self.OPERATION_NAME_SELECT).click()
        self.helper.wait_for_element_visible(f'//div[@id="selectedOperation"]//span[text()="{operationType}"]').click()

        self.helper.wait_for_element_visible('#addOperationBtn').click()
        self.helper.wait_for_element_visible(f'//div[@data-qa="table-route-operations"]//td//span[text()="{routePoint}"]')
        self.helper.wait_for_element_visible(f'//div[@data-qa="table-route-operations"]//td//span[text()="{operationType}"]')

        if unloadPoint:
            self.helper.wait_for_element_visible(f'//td//span[text()="{routePoint}"]//..//..//div[@id="relatedOperation"]').click()
            self.helper.wait_for_element_visible(f'//td//span[text()="{routePoint}"]//..//..//div[@id="relatedOperation"]//div[text()[contains(.,"{unloadPoint}")]]').click()


    @step('Нажать на кнопку "Сохранить маршрут"')
    def saveRoute(self):
        self.helper.wait_for_element_visible(self.SAVE_ROUTE_BUTTON).click()
        self.helper.wait_for_element_invisibility(self.SAVE_ROUTE_BUTTON, 45)

    @step('Проверить что кнопка "Сохранить маршрут" заблокирована')
    def checkLockSaveButton(self):
        self.helper.wait_for_element_visible(self.DISABLE_SAVE_ROUTE_BUTTON)

    @step('Проверить ошибку при создании маршрута с разным ко-вом операций')
    def checkErrorMessageAfterSaveRoute(self, expectedError):
        errorText = '#errorMessage0'

        self.helper.wait_for_element_visible(self.SAVE_ROUTE_BUTTON).click()
        self.helper.wait_for_element_visible(errorText)
        assert (self.helper.wait_for_element_visible(errorText).text == expectedError, 'Сообщение об ошибке не совпадает!')

    @step('Отфильтровать маршруты по первой точке маршрута')
    def filteringRoutesByFirstPoints(self, firstRoutePoint):
        self.helper.wait_for_element_visible(self.FIRST_POINT_FILTER).click()
        self.helper.fill_field('#firstPointFilter input', firstRoutePoint)
        self.helper.wait_for_element_visible(f'//div[@id="firstPointFilter"]//span[text()="{firstRoutePoint}"]').click()

    @step('Проверить что маршруты отфильтровались по фильтру {1}')
    def checkFilteringRoutes(self, filter, filterPoint):
        self.helper.wait_for_element_visible('//*[@id="routesTable"]//td[1]')
        rowCount = len(self.helper.grab_multiple('//*[@id="routesTable"]//tbody//tr'))
        for i in range(rowCount):
            filteringRouteName = self.helper.wait_for_element(f'//*[@id="routesTable"]//tr[{i}]//td[3]').text
            filteringRoutePoints = filteringRouteName.split(' >> ')
            match filter:
                case RouteFilter.FIRST_POINT_FILTER:
                    assert (filteringRoutePoints[0] == filterPoint, 'Первая точка маршрута не совпадает')
                case RouteFilter.ANY_POINT_FILTER:
                    assert (filteringRouteName == filterPoint, 'Точка не содержится в маршруте')
                case RouteFilter.LAST_POINT_FILTER:
                    assert (filteringRoutePoints[-1] == filterPoint, 'Последняя точка маршрута не совпадает')
                case RouteFilter.ROUTE_NAME_FILTER:
                    assert (filteringRouteName == filterPoint, 'Название маршрута не совпадает')

    @step('Отфильтровать маршруты по последней точке маршрута')
    def filteringRoutesByLastPoints(self, lastRoutePoint):
        self.helper.wait_for_element_visible(self.LAST_POINT_FILTER).click()
        self.helper.fill_field('#lastPointFilter input', lastRoutePoint)
        self.helper.wait_for_element_visible(f'//div[@id="lastPointFilter"]//span[text()="{lastRoutePoint}"]').click()

    @step( 'Отфильтровать маршруты по любой точке маршрута')
    def filteringRoutesByAnyPoints(self, anyRoutePoint):
        self.helper.wait_for_element_visible(self.ANY_POINT_FILTER).click()
        self.helper.fill_field('#anyPointFilter input', anyRoutePoint)
        self.helper.wait_for_element_visible(f'//div[@id="anyPointFilter"]//span[text()="{anyRoutePoint}"]').click()

    @step('Отфильтровать маршруты по названию маршрута')
    def filteringRoutesByRouteName(self, routeName):
        self.helper.wait_for_element_visible(self.ROUTE_NAME_FILTER).click()
        self.helper.fill_field('#routeNameFilter input', routeName)
        self.helper.wait_for_element_visible(f'//div[@id="routeNameFilter"]//span[text()="{routeName}"]').click()

    @step('Получить полное название маршрута')
    def getFullRouteName(self, routePoints: List[str]):
        routeName = ''

        if len(routePoints) < 2:
            assert False, 'Маршрут состоит менее чем из двух точек!'
        for i in range(len(routePoints)):
            if i == (len(routePoints) - 1):
                routeName = routeName + routePoints[i]
            else:
                routeName = routeName + routePoints[i] + ' >> '
        return routeName

    @step('Изменить состояние фильтра "Маршруты с активными шаблонами" на {1}')
    def filteringRoutesByActivity(self, isEnable):
        toggle_class = self.helper.grab_attribute('[data-qa="active-switch"] label', 'class')
        current_state = 'active' in toggle_class
        if current_state != isEnable:
            self.helper.wait_for_element_visible('[data-qa="active-switch"] label').click()

    @step('Нажать на кнопку "Очистить фильтр" и проверить что фильтры очистились')
    def clearRouteFilter(self):
        self.helper.wait_for_element_visible('#clearFilters').click()
        assert (self.helper.wait_for_element('(//div[@id="firstPointFilter"]//span)[4]').text, 'Фильтр "Поиск по первой точке" не очищен')
        assert (self.helper.wait_for_element('(//div[@id="anyPointFilter"]//span)[4]').text, 'Фильтр "Поиск по любой точке" не очищен')
        assert (self.helper.wait_for_element('(//div[@id="lastPointFilter"]//span)[4]').text, 'Фильтр "Поиск по последней точке" не очищен')
        assert (self.helper.wait_for_element('(//div[@id="routeNameFilter"]//span)[4]').text, 'Фильтр "Поиск по названию маршрута" не очищен')
        self.helper.wait_for_element_visible('//*[@id="routesTable"]//td[1]')
        rowCount = len(self.helper.grab_multiple('//*[@id="routesTable"]//tbody//tr'))
        assert rowCount < 2, 'В выдаче менее 2ух рейсов! Фильтры не очистились'

    @step('Проверить корректное отображение созданного маршрута')
    def checkCreatedRoute(self, userName, routeName, routeDistrict):
        today = datetime.now().strftime("%d.%m.%Y")
        self.filteringRoutesByRouteName(routeName)
        self.helper.wait_for_element_visible('//*[@id="routesTable"]//td[1]')

        assert (self.helper.wait_for_element('//*[@id="routesTable"]//td[2]').text == today,
                'Дата создания маршрута не совпадает!')
        assert (self.helper.wait_for_element('//*[@id="routesTable"]//td[3]').text == routeName,
                'Наименование маршрута не совпадает!')
        assert (self.helper.wait_for_element('//*[@id="routesTable"]//td[4]').text == routeDistrict,
                'Федеральный округ созданного рейса отличается!')
        assert (self.helper.wait_for_element('//*[@id="routesTable"]//td[5]').text == 'Нет',
                'У созданного рейса есть активные шаблоны!')
        assert (self.helper.wait_for_element('//*[@id="routesTable"]//td[6]').text == userName,
                'Имя пользователя, создавшего рейс, не совпадает!')

    @step('Проверить что маршруты не отображаются')
    def checkEmptyRoute(self):
        self.helper.wait_for_element_invisibility('//*[@id="routesTable"]//td[1]')

    @step('Удалить первый маршрут в списке')
    def deleteFirstRoute(self):
        modalWindow = '[data-qa="modal-delete-route"]'

        self.helper.wait_for_element_visible('#deleteBtn').click()
        self.helper.wait_for_element_visible(modalWindow)
        self.helper.wait_for_element_visible('[data-qa="button-accept"]').click()
        self.helper.wait_for_element_invisibility(modalWindow, 30)
        self.helper.wait_for_element_invisibility('//*[@id="routesTable"]//td[1]', 30)

    @step('Закрыть окно с созданием маршрута')
    def closeCreateRouteWindow(self):
        self.helper.wait_for_element_visible('[data-qa="modal-route-create"] a').click()
        self.helper.wait_for_element_invisibility('[data-qa="modal-route-create"]', 30)

    @step('Проверить что нельзя добавить операцию разгрузки первой строкой')
    def checkLockUnloadOperation(self, routePoint, operationType):
        if self.helper.check_element_on_page(self.ADD_OPERATION_BUTTON):
            self.helper.wait_for_element_visible(self.ADD_OPERATION_BUTTON).click()
        self.helper.wait_for_element_visible(self.POINT_NAME_SELECT).click()
        self.helper.fill_field(self.POINT_NAME_INPUT, routePoint)
        self.helper.wait_for_element_visible(f'//div[@id="pointName"]//span[text()="{routePoint}"]').click()
        self.helper.wait_for_element_visible(self.OPERATION_NAME_SELECT).click()
        self.helper.wait_for_element_visible(f'//div[@id="selectedOperation"]//span[text()="{operationType}"]/parent::div[@class[contains(.,"disabled")]]')
        self.helper.wait_for_element_visible(self.DISABLE_SAVE_ROUTE_BUTTON)

    @step('Проверить операции у открытого на редактирование/созданного на основании маршрута')
    def checkOpenRoute(self, routePointOperations):
        for i in range(len(routePointOperations)):
            assert (self.helper.wait_for_element_visible(
                f'//div[@data-qa="table-route-operations"]//tbody//tr[{i + 1}]//td[1]//span', 2).text == str(i + 1),
                    'Номер операции не совпадает!')
            assert (self.helper.wait_for_element_visible(
                f'//div[@data-qa="table-route-operations"]//tbody//tr[{i + 1}]//td[2]//span', 2).text == routePointOperations[i]['pointName'],
                    'Название точки не совпадает!')
            assert (self.helper.wait_for_element_visible(
                f'//div[@data-qa="table-route-operations"]//tbody//tr[{i + 1}]//td[3]//span', 2).text == routePointOperations[i]['operationType'],
                    'Тип операции не совпадает!')
            if routePointOperations[i]['unloadPoint']:
                assert (self.helper.wait_for_element_visible(
                    f'//div[@data-qa="table-route-operations"]//tbody//tr[{i + 1}]//td[4]//span', 2).text ==
                        routePointOperations[i]['unloadPoint'],
                        'Точка разгрузки не совпадает!')

    @step('Удалить операцию из маршрута по её номеру')
    def deleteOperationInRouteByNumber(self, numberOfOperation):
        self.helper.wait_for_element_visible(f'//div[@data-qa="table-route-operations"]//tbody//tr[{numberOfOperation}]//td[7]//button').click()

    @step('Удалить маршрут из БД по точкам если по маршруту не было рейсов')
    def deleteRouteFromDbByPoints(self, db_connection, routeName):
        db = SqlQueries(db_connection)
        routePoints = routeName.split(' >> ')
        countTrips = db.get_trips_by_route_name(routeName)
        countRoutes = db.get_routes_by_route_name(routeName)

        if countRoutes[0]['kolvo'] != 0:
            if countTrips[0]['kolvo'] == 0:
                route_id = db.get_route_data_by_route_name(routeName)
                for k in range(len(routePoints)):
                    route_pont_id = db.get_route_point_by_route_id(route_id)
                    db.delete_route_operation_by_route_point_id(route_pont_id)
                    db.delete_route_point_by_route_point_id(route_pont_id)
                db.delete_route_point_by_route_id(route_id)
                db.delete_route_by_route_name(routeName)
                assert True, 'Маршрут удален из БД'
            else:
                assert False, 'По маршруту были созданы рейсы, нельзя удалять!'
        else:
            assert False, 'Маршрут не создан, удаление из БД не требуется'