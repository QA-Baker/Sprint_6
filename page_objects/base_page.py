from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_yandex_logo(self):
        yandex_logo = self.wait.until(ec.element_to_be_clickable(BasePageLocators.yandex_logo))
        yandex_logo.click()

    def click_scooter_logo(self):
        scooter_logo = self.wait.until(ec.element_to_be_clickable(BasePageLocators.scooter_logo))
        scooter_logo.click()

    def click_top_order_button(self):
        top_order_button = self.wait.until(ec.element_to_be_clickable(BasePageLocators.top_order_button))
        top_order_button.click()

    def click_bottom_order_button(self):
        bottom_order_button = self.wait.until(ec.element_to_be_clickable(BasePageLocators.bottom_order_button))
        bottom_order_button.click()
