import os
import allure
import datetime
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="function")
def driver(request):
    """
    Получение объекта webdriver с возможностью сделать скриншот при падении автотеста
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
    if not request.node.rep_call.passed:
        take_screenshot(driver, test_name)
        url_error = f"Url на котором упал автотест {driver.current_url}"
        with allure.step(url_error):
            pass
        print(f"Сделан скриншот места падения теста\n{url_error}\n")
    print("\nЗавершить сеанс браузера...")
    driver.quit()


def get_webdriver():
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


def get_chrome_options(headless=True):
    """
    Получение настроек для браузера chrome
    :return:
    """
    options = chrome_options()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    if headless:
        options.add_argument("--headless")
    return options


def take_screenshot(driver: WebDriver, test_name):
    """
    Делаем скриншот
    :param driver: объект webdriver
    :param test_name: имя теста
    """
    date_now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = f"{test_name}_{date_now}.png"
    os.makedirs(os.path.join(DIRECTORY_PATH, "_output"), exist_ok=True)
    screenshot_file_path = os.path.join(DIRECTORY_PATH, "_output", filename)
    png = driver.get_screenshot_as_png()
    allure.attach(
        png, name="Скриншот места падения теста", attachment_type=AttachmentType.PNG
    )

    with open(screenshot_file_path, "wb") as f:
        f.write(png)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
