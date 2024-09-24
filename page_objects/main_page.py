from locators.base_page_locators import BasePageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    def click_scooter_logo(self):
        self.click_element(BasePageLocators.scooter_logo)

    def click_yandex_logo(self):
        self.click_element(BasePageLocators.yandex_logo)

    def click_faq_question(self, locator):
        self.click_element(locator)

    def check_faq_answer_displayed(self, locator):
        element = self.find_element(locator)
        return element.is_displayed()
