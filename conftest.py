import os
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from _pytest.fixtures import FixtureRequest
from api_utils.api_client import ApiClient
from utils import db_connect as DataBase


@pytest.fixture(scope="function")
def driver(request: FixtureRequest) -> WebDriver:
    """
    Получение объекта webdriver
    """
    test_name = request.node.name
    print(
        "_________________________________"
        + test_name
        + "_________________________________"
        + "\n\n"
    )
    driver = get_webdriver()
    if request.cls is not None:
        request.cls.driver = driver
    print("Запустить браузер для тестов...\n")
    yield driver
    print("\nЗавершить сеанс браузера...")
    driver.quit()


def get_webdriver() -> WebDriver:
    """
    Получение объекта webdriver
    :return: объект webdriver
    """
    selenium_remote = os.getenv("SELENIUM_REMOTE")
    if selenium_remote:
        opts = get_chrome_options()
        return webdriver.Remote(
            command_executor=selenium_remote,
            options=opts
        )
    else:
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=get_chrome_options(False),
        )


def get_chrome_options(headless=True) -> ChromeOptions:
    """
    Получение настроек для браузера chrome
    :return:
    """
    options = ChromeOptions()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    if headless:
        options.add_argument("--headless")
    return options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "driver" in item.fixturenames:
                driver: WebDriver = item.funcargs["driver"]
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="Скриншот места падения теста",
                    attachment_type=AttachmentType.PNG,
                )
        except Exception:
            print("Не удалось получить скриншот")


@pytest.fixture(scope='session')
def client():
    return ApiClient()


@pytest.fixture(scope='session', autouse=True)
def db_connection():
    connection = DataBase.open_connection()
    yield connection
    DataBase.close_connection()
