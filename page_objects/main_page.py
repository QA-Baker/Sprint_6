from locators.main_page_locators import MainPageLocators


class MainPageMethods:
    def __init__(self, driver):
        self.driver = driver
        self.locators = MainPageLocators()

    def click_price_and_payment(self):
        element = self.driver.find_element(*self.locators.price_and_payment)
        element.click()

    def click_multiple_scooters(self):
        element = self.driver.find_element(*self.locators.multiple_scooters)
        element.click()

    def click_rental_time_calculation(self):
        element = self.driver.find_element(*self.locators.rental_time_calculation)
        element.click()

    def click_order_today(self):
        element = self.driver.find_element(*self.locators.order_today)
        element.click()

    def click_extend_or_return(self):
        element = self.driver.find_element(*self.locators.extend_or_return)
        element.click()

    def click_charger_included(self):
        element = self.driver.find_element(*self.locators.charger_included)
        element.click()

    def click_cancel_order(self):
        element = self.driver.find_element(*self.locators.cancel_order)
        element.click()

    def click_outside_mkad(self):
        element = self.driver.find_element(*self.locators.outside_mkad)
        element.click()
