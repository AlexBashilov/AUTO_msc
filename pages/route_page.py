import allure
from helperpackage import HelperWd


class RoutePage:
    CREATE_BUTTON = '#createBtn'
    SAVE_ROUTE_BUTTON = '#upsertRouteBtn'
    DISABLE_SAVE_ROUTE_BUTTON = '//button[@id="upsertRouteBtn"][@disabled=""]'
    FIRST_POINT_FILTER = '#firstPointFilter'
    LAST_POINT_FILTER = '#lastPointFilter'
    ANY_POINT_FILTER = '#anyPointFilter'
    ROUTE_NAME_FILTER = '#routeNameFilter'
    TOOLTIP_LABEL = '[data-qa="note-wrapper"]'
    ADD_OPERATION_BUTTON = '#startAddingOperationBtn'
    POINT_NAME_SELECT = '#pointName'
    POINT_NAME_INPUT = '#pointName input'
    OPERATION_NAME_SELECT = '#selectedOperation'

    def __init__(self, driver):
        self.helper = HelperWd(driver)

    @allure.step('Проверить наименование активных элементов на странице')
    def check_route_page_elements(self):
        self.helper.wait_for_element_visible('h2')
        assert self.helper.wait_for_element_visible('h2').text == 'Маршруты'
        self.helper.wait_for_element_visible('[data-qa="active-switch"]')
        assert self.helper.wait_for_element_visible(
            '[data-qa="active-switch"]').text == 'Маршруты с шаблонами'
        self.helper.wait_for_element_visible('#clearFilters')
        assert self.helper.wait_for_element_visible('#clearFilters').text == 'Очистить фильтры'
        self.helper.wait_for_element_visible(self.CREATE_BUTTON)
        assert self.helper.wait_for_element_visible(self.CREATE_BUTTON).text == 'Создать новый маршрут'
        self.helper.wait_for_element_visible(self.FIRST_POINT_FILTER)
        assert self.helper.wait_for_element_visible(self.FIRST_POINT_FILTER).text == 'Поиск по первой точке'
        self.helper.wait_for_element_visible('#anyPointFilter')
        assert self.helper.wait_for_element_visible('#anyPointFilter').text == 'Поиск по любой точке'
        self.helper.wait_for_element_visible(self.LAST_POINT_FILTER)
        assert self.helper.wait_for_element_visible(self.LAST_POINT_FILTER).text == 'Поиск по последней точке'
        self.helper.wait_for_element_visible('#routeNameFilter')
        assert self.helper.wait_for_element_visible('#routeNameFilter').text == 'Поиск по названию маршрута'

    @allure.step('Нажать на кнопку "Создать маршрут"')
    def create_route(self):
        self.helper.wait_for_element_visible(self.CREATE_BUTTON).click()
        self.helper.wait_for_element_visible(self.DISABLE_SAVE_ROUTE_BUTTON)
        assert (self.helper.wait_for_element_visible(self.TOOLTIP_LABEL).text ==
                'Значения в колонке "Разгрузка из" будут сбрасываться, после каждого изменения. Внести значения '
                'необходимо перед сохранением маршрута'), \
            'Текст тултипа не совпадает!'

    @allure.step('Нажать на кнопку "Создать на основании" у первого маршрута')
    def create_route_based_on(self):
        self.helper.wait_for_element_visible('[data-qa="create-on-based"]').click()
        # Добавил тут вейт, потому что дальше не отрабатывает удаление... Оно видит иконку и
        # кликает по ней, но операция не удаляется, я не смог понять почему
        self.helper.wait_(1)
        self.helper.wait_for_element_visible('//button[@id="upsertRouteBtn"]')
        assert (self.helper.wait_for_element_visible(self.TOOLTIP_LABEL).text ==
                'Значения в колонке "Разгрузка из" будут сбрасываться, после каждого изменения. Внести '
                'значения необходимо перед сохранением маршрута'), \
            'Текст тултипа не совпадает!'

    #
    # def addOperationInRoute(string $routePoint, string $operationType, string $unloadPoint = null): void
    #
    #     Allure::runStep(
    #         function () use ($routePoint, $operationType, $unloadPoint)
    #             $I = $this->tester
    #             if ($I->checkElementOnPage(self.ADD_OPERATION_BUTTON))
    #                 $I->click(self.ADD_OPERATION_BUTTON)
    #
    #             self.helper.wait_for_element_visible.click()(self.POINT_NAME_SELECT)
    #             $I->fillFieldAfterWaitingElementVisible(self.POINT_NAME_INPUT, $routePoint)
    #             self.helper.wait_for_element_visible.click()('//div[@id="pointName"]//span[text()="' . $routePoint . '"]')
    #
    #             self.helper.wait_for_element_visible.click()(self.OPERATION_NAME_SELECT)
    #             self.helper.wait_for_element_visible.click()('//div[@id="selectedOperation"]//span[text()="' . $operationType . '"]')
    #
    #             $I->click('#addOperationBtn')
    #             self.helper.wait_for_element_visible('//div[@data-qa="table-route-operations"]//td//span[text()="' . $routePoint . '"]')
    #             self.helper.wait_for_element_visible('//div[@data-qa="table-route-operations"]//td//span[text()="' . $operationType . '"]')
    #
    #             if ($unloadPoint)
    #                 self.helper.wait_for_element_visible.click()('//td//span[text()="' . $routePoint . '"]//..//..//div[@id="relatedOperation"]')
    #                 self.helper.wait_for_element_visible.click()('//td//span[text()="' . $routePoint . '"]//..//..//div[@id="relatedOperation"]//div[text()[contains(.,"' . $unloadPoint . '")]]')
    #
    #
    #         'Добавить операцию в маршрут. Название точки - ' . $routePoint . '. Операция - ' . $operationType . '.'
    #     )
    #
    #
    # def saveRoute(self):
    #
    #
    #             $I->clickOnElementAfterWaitingItClickable(self.SAVE_ROUTE_BUTTON)
    #             $I->waitForElementNotVisible(self.SAVE_ROUTE_BUTTON, 45)
    #
    #         'Нажать на кнопку "Сохранить маршрут"'
    #     )
    #
    #
    # def checkLockSaveButton(self):
    #
    #     Allure::runStep(
    #         function ()
    #             $this->tester->waitForElementVisible(self.DISABLE_SAVE_ROUTE_BUTTON)
    #
    #         'Проверить что кнопка "Сохранить маршрут" заблокирована'
    #     )
    #
    #
    # def checkErrorMessageAfterSaveRoute(string $expectedError): void
    #
    #     Allure::runStep(
    #         function () use ($expectedError)
    #             $I = $this->tester
    #             $errorText = '#errorMessage0'
    #
    #             $I->clickOnElementAfterWaitingItClickable(self.SAVE_ROUTE_BUTTON)
    #             self.helper.wait_for_element_visible($errorText)
    #             $errorMessage = $I->grabTextFrom($errorText)
    #             $I->assertStringContainsString($expectedError, $errorMessage, 'Сообщение об ошибке не совпадает!')
    #
    #         'Проверить ошибку при создании маршрута с разным ко-вом операций'
    #     )
    #
    #
    # def filteringRoutesByFirstPoints(string $firstRoutePoint): void
    #
    #     Allure::runStep(
    #         function () use ($firstRoutePoint)
    #             $I = $this->tester
    #             self.helper.wait_for_element_visible.click()(self.FIRST_POINT_FILTER)
    #             $I->fillFieldAfterWaitingElementVisible('#firstPointFilter input', $firstRoutePoint)
    #             self.helper.wait_for_element_visible.click()('//div[@id="firstPointFilter"]//span[text()="' . $firstRoutePoint . '"]')
    #
    #         'Отфильтровать маршруты по первой точке маршрута'
    #     )
    #
    #
    # def checkFilteringRoutes(string $filter, string $filterPoint): void
    #
    #     Allure::runStep(
    #         function () use ($filter, $filterPoint)
    #             $I = $this->tester
    #             self.helper.wait_for_element_visible('//*[@id="routesTable"]//td[1]')
    #             $rowCount = count($I->grabMultiple('//*[@id="routesTable"]//tbody//tr'))
    #             for ($i = 1 $i <= $rowCount ++$i)
    #                 $filteringRouteName = $I->grabTextFrom('//*[@id="routesTable"]//tr[' . $i . ']//td[3]')
    #                 $filteringRoutePoints = explode(' >> ', $filteringRouteName)
    #                 switch ($filter)
    #                     case RouteFilter::FIRST_POINT_FILTER:
    #                         $I->assertEquals($filterPoint, $filteringRoutePoints[0], 'Первая точка маршрута не совпадает')
    #
    #                         break
    #                     case RouteFilter::ANY_POINT_FILTER:
    #                         $I->assertStringContainsString($filterPoint, $filteringRouteName, 'Точка не содержится в маршруте')
    #
    #                         break
    #                     case RouteFilter::LAST_POINT_FILTER:
    #                         $I->assertEquals($filterPoint, end($filteringRoutePoints), 'Последняя точка маршрута не совпадает')
    #
    #                         break
    #                     case RouteFilter::ROUTE_NAME_FILTER:
    #                         $I->assertEquals($filterPoint, $filteringRouteName, 'Название маршрута не совпадает')
    #
    #                         break
    #
    #
    #
    #         'Проверить что маршруты отфильтровались по фильтру "' . $filter . '"'
    #     )
    #
    #
    # def filteringRoutesByLastPoints(string $lastRoutePoint): void
    #
    #     Allure::runStep(
    #         function () use ($lastRoutePoint)
    #             $I = $this->tester
    #             self.helper.wait_for_element_visible.click()(self.LAST_POINT_FILTER)
    #             $I->fillFieldAfterWaitingElementVisible('#lastPointFilter input', $lastRoutePoint)
    #             self.helper.wait_for_element_visible.click()('//div[@id="lastPointFilter"]//span[text()="' . $lastRoutePoint . '"]')
    #
    #         'Отфильтровать маршруты по последней точке маршрута'
    #     )
    #
    #
    # def filteringRoutesByAnyPoints(string $anyRoutePoint): void
    #
    #     Allure::runStep(
    #         function () use ($anyRoutePoint)
    #             $I = $this->tester
    #             self.helper.wait_for_element_visible.click()(self.ANY_POINT_FILTER)
    #             $I->fillFieldAfterWaitingElementVisible('#anyPointFilter input', $anyRoutePoint)
    #             self.helper.wait_for_element_visible.click()('//div[@id="anyPointFilter"]//span[text()="' . $anyRoutePoint . '"]')
    #
    #         'Отфильтровать маршруты по любой точке маршрута'
    #     )
    #
    #
    # def filteringRoutesByRouteName(string $routeName): void
    #
    #     Allure::runStep(
    #         function () use ($routeName)
    #             $I = $this->tester
    #             self.helper.wait_for_element_visible.click()(self.ROUTE_NAME_FILTER)
    #             $I->fillFieldAfterWaitingElementVisible('#routeNameFilter input', $routeName)
    #             self.helper.wait_for_element_visible.click()('//div[@id="routeNameFilter"]//span[text()="' . $routeName . '"]')
    #
    #         'Отфильтровать маршруты по названию маршрута'
    #     )
    #
    #
    # def getFullRouteName(array $routePoints): mixed
    #
    #     return Allure::runStep(
    #         function () use ($routePoints)
    #             $I = $this->tester
    #             $routeName = ''
    #
    #             if (count($routePoints) < 2)
    #                 $I->assertTrue(true, 'Маршрут состоит менее чем из двух точек!')
    #
    #
    #             for ($i = 0 $i < count($routePoints) ++$i)
    #                 if ($i == (count($routePoints) - 1))
    #                     $routeName = $routeName . $routePoints[$i]
    #                  else
    #                     $routeName = $routeName . $routePoints[$i] . ' >> '
    #
    #
    #
    #             return $routeName
    #
    #         'Получить полное название маршрута'
    #     )
    #
    #
    # def filteringRoutesByActivity(bool $isEnable): void
    #
    #     Allure::runStep(
    #         function () use ($isEnable)
    #             $I = $this->tester
    #             $toggleClass = $I->grabAttributeFrom('[data-qa="active-switch"] label', 'class')
    #             $currentState = str_contains($toggleClass, 'active')
    #             if ($currentState != $isEnable)
    #                 self.helper.wait_for_element_visible.click()('[data-qa="active-switch"] label')
    #
    #
    #         'Изменить состояние фильтра "Маршруты с активными шаблонами" на ' . $isEnable
    #     )
    #
    #
    # def clearRouteFilter(self):
    #
    #
    #             self.helper.wait_for_element_visible.click()('#clearFilters')
    #             $I->assertEmpty($I->grabTextFrom('(//div[@id="firstPointFilter"]//span)[4]'), 'Фильтр "Поиск по первой точке" не очищен')
    #             $I->assertEmpty($I->grabTextFrom('(//div[@id="anyPointFilter"]//span)[4]'), 'Фильтр "Поиск по любой точке" не очищен')
    #             $I->assertEmpty($I->grabTextFrom('(//div[@id="lastPointFilter"]//span)[4]'), 'Фильтр "Поиск по последней точке" не очищен')
    #             $I->assertEmpty($I->grabTextFrom('(//div[@id="routeNameFilter"]//span)[4]'), 'Фильтр "Поиск по названию маршрута" не очищен')
    #             self.helper.wait_for_element_visible('//*[@id="routesTable"]//td[1]')
    #             $rowCount = count($I->grabMultiple('//*[@id="routesTable"]//tbody//tr'))
    #             $I->assertGreaterThan(2, $rowCount, 'В выдаче менее 2ух рейсов! Фильтры не очистились')
    #
    #         'Нажать на кнопку "Очистить фильтр" и проверить что фильтры очистились'
    #     )
    #
    #
    # def checkCreatedRoute(string $userName, string $routeName): void
    #
    #     Allure::runStep(
    #         function () use ($userName, $routeName)
    #             $this->tester->waitDuringIteration(
    #                 function () use ($userName, $routeName)
    #                     $I = $this->tester
    #                     $today = date('d.m.Y')
    #
    #                     self.filteringRoutesByRouteName($routeName)
    #                     self.helper.wait_for_element_visible('//*[@id="routesTable"]//td[1]')
    #
    #                     $routeDate = $I->grabTextFrom('//*[@id="routesTable"]//td[2]')
    #                     $I->assertEquals($today, $routeDate, 'Дата создания маршрута не совпадает!')
    #
    #                     $haveActiveTemplate = $I->grabTextFrom('//*[@id="routesTable"]//td[4]')
    #                     $I->assertEquals('Нет', $haveActiveTemplate, 'У созданного рейса есть активные шаблоны!')
    #
    #                     $createUserName = $I->grabTextFrom('//*[@id="routesTable"]//td[5]')
    #                     $I->assertEquals($userName, $createUserName, 'Имя пользователя, создавшего рейс, не совпадает!')
    #
    #                 'Созданный маршрут отображается некорректно!',
    #                 10,
    #                 function ()
    #                     $this->tester->wait(1)
    #                     $this->tester->reloadPage()
    #
    #             )
    #
    #         'Проверить корректное отображение созданного маршрута'
    #     )
    #
    #
    # def checkEmptyRoute(self):
    #
    #
    #             $I->waitForElementNotVisible('//*[@id="routesTable"]//td[1]')
    #
    #         'Проверить что маршруты не отображаются'
    #     )
    #
    #
    # def deleteFirstRoute(self):
    #
    #
    #             $modalWindow = '[data-qa="modal-delete-route"]'
    #
    #             self.helper.wait_for_element_visible.click()('#deleteBtn')
    #             self.helper.wait_for_element_visible($modalWindow)
    #             $I->click('[data-qa="button-accept"]')
    #             $I->waitForElementNotVisible($modalWindow, 30)
    #             $I->waitForElementNotVisible('//*[@id="routesTable"]//td[1]', 30)
    #
    #         'Удалить первый маршрут в списке'
    #     )
    #
    #
    # def closeCreateRouteWindow(self):
    #
    #
    #
    #             self.helper.wait_for_element_visible.click()('[data-qa="modal-route-create"] a')
    #             $I->waitForElementNotVisible('[data-qa="modal-route-create"]', 30)
    #
    #         'Закрыть окно с созданием маршрута'
    #     )
    #
    #
    # def checkLockUnloadOperation(string $routePoint, string $operationType): void
    #
    #     Allure::runStep(
    #         function () use ($routePoint, $operationType)
    #             $I = $this->tester
    #             if ($I->checkElementOnPage(self.ADD_OPERATION_BUTTON))
    #                 $I->click(self.ADD_OPERATION_BUTTON)
    #
    #             self.helper.wait_for_element_visible.click()(self.POINT_NAME_SELECT)
    #             $I->fillFieldAfterWaitingElementVisible(self.POINT_NAME_INPUT, $routePoint)
    #             self.helper.wait_for_element_visible.click()('//div[@id="pointName"]//span[text()="' . $routePoint . '"]')
    #
    #             self.helper.wait_for_element_visible.click()(self.OPERATION_NAME_SELECT)
    #             self.helper.wait_for_element_visible('//div[@id="selectedOperation"]//span[text()="' . $operationType . '"]/parent::div[@class[contains(.,"disabled")]]')
    #             self.helper.wait_for_element_visible(self.DISABLE_SAVE_ROUTE_BUTTON)
    #
    #         'Проверить что нельзя добавить операцию разгрузки первой строкой'
    #     )
    #
    #
    # def checkOpenRoute(array $routePointOperations): void
    #
    #     Allure::runStep(
    #         function () use ($routePointOperations)
    #             $I = $this->tester
    #             for ($i = 0 $i < count($routePointOperations) ++$i)
    #                 $I->assertEquals(strval($i + 1), $I->grabTextFrom('//div[@data-qa="table-route-operations"]//tbody//tr[' . $i + 1 . ']//td[1]//span'), 'Номер операции не совпадает!')
    #                 $I->assertEquals($routePointOperations[$i]['pointName'], $I->grabTextFrom('//div[@data-qa="table-route-operations"]//tbody//tr[' . $i + 1 . ']//td[2]//span'), 'Название точки не совпадает!')
    #                 $I->assertEquals($routePointOperations[$i]['operationType'], $I->grabTextFrom('//div[@data-qa="table-route-operations"]//tbody//tr[' . $i + 1 . ']//td[3]//span'), 'Тип операции не совпадает!')
    #                 if ($routePointOperations[$i]['unloadPoint'] != null)
    #                     $I->assertStringContainsString($routePointOperations[$i]['unloadPoint'], $I->grabTextFrom('//div[@data-qa="table-route-operations"]//tbody//tr[' . $i + 1 . ']//td[4]//div//div//span[2]'), 'Точка разгрузки не совпадает!')
    #
    #
    #
    #         'Проверить операции у открытого на редактирование/созданного на основании маршрута'
    #     )
    #
    #
    # def deleteOperationInRouteByNumber(int $numberOfOperation): void
    #
    #     Allure::runStep(
    #         function () use ($numberOfOperation)
    #             $I = $this->tester
    #             self.helper.wait_for_element_visible.click()('//div[@data-qa="table-route-operations"]//tbody//tr[' . $numberOfOperation . ']//td[7]//button')
    #
    #         'Удалить операцию из маршрута по её номеру'
    #     )
    #
