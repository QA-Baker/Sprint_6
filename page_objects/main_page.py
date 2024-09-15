from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPageMethods(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def click_price_and_payment(self):
        self.click_element(self.locators.price_and_payment)

    def click_multiple_scooters(self):
        self.click_element(self.locators.multiple_scooters)

    def click_rental_time_calculation(self):
        self.click_element(self.locators.rental_time_calculation)

    def click_order_today(self):
        self.click_element(self.locators.order_today)

    def click_extend_or_return(self):
        self.click_element(self.locators.extend_or_return)

    def click_charger_included(self):
        self.click_element(self.locators.charger_included)

    def click_cancel_order(self):
        self.click_element(self.locators.cancel_order)

    def click_outside_mkad(self):
        self.click_element(self.locators.outside_mkad)
