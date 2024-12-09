import os

import allure
from helperpackage import HelperWd


class Login:
    def __init__(self, driver):
        self.helper = HelperWd(driver)

    @allure.step(
        "Получить данные для авторизации под разными пользователя для каждого потока"
    )
    def get_credentials(self) -> dict:
        userCredentials = {
            "login": os.getenv("TMS_USER_LOGIN"),
            "password": os.getenv("TMS_USER_PASS"),
            "username": os.getenv("TMS_USER_LOGIN").replace('_', '-'),
        }

        return userCredentials

    @allure.step("Выполнить логин в системе TMS")
    def login_to_TMS(self) -> dict:
        login_field = '[name="user_name"][type="text"]'
        user_credentials = self.get_credentials()
        login_button = "#signInBtn"

        try:
            self.helper.wait_for_element_visible(login_button).click()
            self.helper.wait_for_element_visible(login_field)
        except Exception:
            self.helper.wait_for_element_visible(login_button).click()
            self.helper.wait_for_element_visible(login_field)

        self.helper.fill_field(login_field, user_credentials["login"])
        self.helper.fill_field(
            '[name="user_password"][type="password"]', user_credentials["password"]
        )
        self.helper.wait_for_element_visible(
            '//h1[text()="Вход"]/following::a[contains(@class , "primary")]'
        ).click()
        try:
            self.helper.wait_for_element_visible(".b9lk9-", 10)
            self.helper.wait_for_element_invisibility(".b9lk9-", 30)
        except Exception:
            self.helper.wait_for_element_invisibility(".b9lk9-", 30)
        self.helper.wait_for_element_visible("#accountBtn")

        return user_credentials
