import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from config import BASE_URL, ORDER_URL, ORDER_STATUS_URL, DZEN_URL


@pytest.fixture(scope="function")
def create_driver():
    gecko_path = "D:/Программы/WebDriver/bin/geckodriver.exe"
    firefox_binary_path = "C:/Program Files/Mozilla Firefox/firefox.exe"
    firefox_options = Options()
    firefox_options.binary_location = firefox_binary_path
    driver = webdriver.Firefox(service=FirefoxService(executable_path=gecko_path), options=firefox_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(create_driver):
    create_driver.get(BASE_URL)
    return create_driver


@pytest.fixture(scope="function")
def order_page(create_driver):
    create_driver.get(ORDER_URL)
    return create_driver


@pytest.fixture(scope="function")
def order_status_page(create_driver):
    create_driver.get(ORDER_STATUS_URL)
    return create_driver


@pytest.fixture(scope="function")
def dzen_page(create_driver):
    create_driver.get(DZEN_URL)
    return create_driver
