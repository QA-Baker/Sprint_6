from selenium.webdriver import Keys

from page_objects.base_page import BasePage
from locators.order_page_locators import OrderPage as OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Методы для первой страницы (Про аренду)
    def input_first_name(self, first_name: str):
        self.enter_text(OrderPageLocators.first_name_field, first_name)

    def input_last_name(self, last_name: str):
        self.enter_text(OrderPageLocators.last_name_field, last_name)

    def input_address(self, address: str):
        self.enter_text(OrderPageLocators.address_field, address)

    def select_metro_station(self, metro_name: str):
        self.click_element(OrderPageLocators.metro_station_field)
        self.enter_text(OrderPageLocators.metro_station_field, metro_name)
        metro_option_locator = OrderPageLocators.metro_option_template[0].format(metro_name=metro_name)
        self.click_element((OrderPageLocators.metro_option_template[1], metro_option_locator))

    def input_phone_number(self, phone_number: str):
        self.enter_text(OrderPageLocators.phone_number_field, phone_number)

    def click_next_button(self):
        self.click_element(OrderPageLocators.next_button)

    # Методы для второй страницы (Про аренду)
    def input_rent_date(self, rent_date: str):
        self.click_element(OrderPageLocators.rent_date_field)
        self.enter_text(OrderPageLocators.rent_date_field, rent_date)
        self.driver.find_element(*OrderPageLocators.rent_date_field).send_keys(Keys.ENTER)

    def select_rent_term(self, term: str):
        self.click_element(OrderPageLocators.rent_term_dropdown)
        rent_term_option_locator = OrderPageLocators.rent_term_option_template[0].format(term=term)
        self.click_element((OrderPageLocators.rent_term_option_template[1], rent_term_option_locator))

    def select_scooter_color(self, color: str):
        if color.lower() == 'black':
            self.click_element(OrderPageLocators.scooter_color_black)
        elif color.lower() == 'grey':
            self.click_element(OrderPageLocators.scooter_color_grey)

    def input_courier_comment(self, comment: str):
        self.enter_text(OrderPageLocators.courier_comment_field, comment)

    def click_middle_order_button(self):
        self.click_element(OrderPageLocators.middle_order_button)

    def click_confirm_order_button(self):
        self.click_element(OrderPageLocators.confirm_order_button)

    def is_view_status_button_visible(self):
        return self.find_element(OrderPageLocators.view_status_button).is_displayed()
