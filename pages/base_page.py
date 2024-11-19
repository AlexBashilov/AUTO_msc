import os
import allure
from helperpackage import HelperWd


class Base:
    CANCEL_BUTTON = '//span[text()="Отмена"]/ancestor::button'
    CREATE_BUTTON = "#createBtn"
    SAVE_BUTTON = '[data-qa="btn-save"]'
    ACCEPT_BUTTON = '[data-qa="button-accept"]'
    BURGER_MENU_BUTTON = "#burgerBtn"

    def __init__(self, driver):
        self.helper = HelperWd(driver)
        self.driver = driver

    @allure.step("Перейти на главную страницу TMS")
    def go_to_main_page(self):
        self.helper.go_to_link(
            "https://tms-ui-web.intgr-test-" + self.get_stage() + ".ox1.dev"
        )

    @allure.step("Получить номер стенда")
    def get_stage(self) -> str:
        return os.getenv("STAGE")

    @allure.step("Перейти на страницу 'Маршруты'")
    def go_to_routes_page(self):
        self.helper.wait_for_element_clickable(self.BURGER_MENU_BUTTON).click()
        self.helper.wait_for_element_visible("#routesMenuItem").click()
        self.helper.wait_for_element_visible(".routes-page")

    @allure.step("Перейти на страницу 'Транспортные компании'")
    def go_to_transport_companies_page(self):
        self.helper.wait_for_element_clickable(self.BURGER_MENU_BUTTON).click()
        self.helper.wait_for_element_visible("#transportCompaniesMenuItem").click()
        self.helper.wait_for_element_visible('//h2[text()="Транспортные компании"]')
        self.helper.wait_for_element_visible("//tbody//tr[1]")

    @allure.step("Закрыть модальное окно с информацией")
    def close_info_modal(self):
        self.helper.wait_for_element_clickable(self.CANCEL_BUTTON).click()
        self.helper.wait_for_element_invisibility(self.CANCEL_BUTTON)

    @allure.step("Обновить текущую страницу")
    def refresh_page(self):
        self.driver.refresh()