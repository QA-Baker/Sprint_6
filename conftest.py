import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from config import BASE_URL, ORDER_STATUS_URL, DZEN_URL
from page_objects.base_page import BasePage
from page_objects.order_page import OrderPageMethods


@pytest.fixture(scope="function")
def create_driver():
    gecko_path = os.environ.get("GECKODRIVER_PATH")
    firefox_binary_path = os.environ.get("FIREFOX_BINARY_PATH")

    if not gecko_path or not firefox_binary_path:
        raise EnvironmentError(
            "Переменные окружения GECKODRIVER_PATH или FIREFOX_BINARY_PATH не заданы. "
            "Пожалуйста, задайте их в вашей системе или CI."
        )

    firefox_options = Options()
    firefox_options.binary_location = firefox_binary_path
    driver = webdriver.Firefox(service=FirefoxService(executable_path=gecko_path), options=firefox_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(create_driver):
    create_driver.get(BASE_URL)
    return BasePage(create_driver)


@pytest.fixture(scope="function")
def order_page(create_driver):
    create_driver.get(BASE_URL)
    return OrderPageMethods(create_driver)


@pytest.fixture(scope="function")
def order_status_page(create_driver):
    create_driver.get(ORDER_STATUS_URL)
    return create_driver


@pytest.fixture(scope="function")
def dzen_page(create_driver):
    create_driver.get(DZEN_URL)
    return create_driver
