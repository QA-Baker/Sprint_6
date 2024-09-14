from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.order_page_locators import OrderPage


class OrderPageMethods:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    # Методы для первой страницы (Про аренду)
    def input_first_name(self, first_name: str):
        element = self.wait.until(ec.visibility_of_element_located(OrderPage.first_name_field))
        element.clear()
        element.send_keys(first_name)

    def input_last_name(self, last_name: str):
        element = self.wait.until(ec.visibility_of_element_located(OrderPage.last_name_field))
        element.clear()
        element.send_keys(last_name)

    def input_address(self, address: str):
        element = self.wait.until(ec.visibility_of_element_located(OrderPage.address_field))
        element.clear()
        element.send_keys(address)

    def select_metro_station(self, metro_name: str):
        # Поиск и клик по полю ввода станции метро
        metro_input = self.wait.until(ec.element_to_be_clickable(OrderPage.metro_station_field))
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro_name)

        # Формирование локатора для нужной станции метро
        metro_option_locator = OrderPage.metro_option_template[0].format(metro_name=metro_name)

        # Поиск и клик по нужной станции метро
        metro_option = self.wait.until(
            ec.element_to_be_clickable((OrderPage.metro_option_template[1], metro_option_locator))
        )
        metro_option.click()

    def input_phone_number(self, phone_number: str):
        element = self.wait.until(ec.visibility_of_element_located(OrderPage.phone_number_field))
        element.clear()
        element.send_keys(phone_number)

    def click_next_button(self):
        next_button = self.wait.until(ec.element_to_be_clickable(OrderPage.next_button))
        next_button.click()

    # Методы для второй страницы (Про аренду)
    def input_rent_date(self, rent_date: str):
        date_field = self.wait.until(ec.element_to_be_clickable(OrderPage.rent_date_field))
        date_field.click()
        date_field.clear()
        date_field.send_keys(rent_date)
        date_field.send_keys(Keys.ENTER)
        self.wait.until(ec.invisibility_of_element_located(OrderPage.date_picker_container))

    def select_rent_term(self, term: str):
        term_dropdown = self.wait.until(ec.element_to_be_clickable(OrderPage.rent_term_dropdown))
        term_dropdown.click()

        self.wait.until(ec.visibility_of_element_located(OrderPage.rent_term_menu))

        rent_term_option_locator = OrderPage.rent_term_option_template[0].format(term=term)

        term_option = self.wait.until(
            ec.element_to_be_clickable((OrderPage.rent_term_option_template[1], rent_term_option_locator)))
        term_option.click()

    def select_scooter_color(self, color: str):
        if color.lower() == 'black':
            color_checkbox = self.wait.until(ec.element_to_be_clickable(OrderPage.scooter_color_black))
            color_checkbox.click()
        elif color.lower() == 'grey':
            color_checkbox = self.wait.until(ec.element_to_be_clickable(OrderPage.scooter_color_grey))
            color_checkbox.click()

    def input_courier_comment(self, comment: str):
        comment_field = self.wait.until(ec.visibility_of_element_located(OrderPage.courier_comment_field))
        comment_field.clear()
        comment_field.send_keys(comment)

    def click_middle_order_button(self):
        middle_order_button = self.wait.until(ec.element_to_be_clickable(OrderPage.middle_order_button))
        middle_order_button.click()

    # Метод для клика по кнопке "Да" в модальном окне подтверждения заказа
    def click_confirm_order_button(self):
        confirm_button = self.wait.until(ec.visibility_of_element_located(OrderPage.confirm_order_button))
        confirm_button.click()

    # Метод для клика по кнопке "Посмотреть статус" после оформления заказа
    def click_view_status_button(self):
        view_status_button = self.wait.until(ec.element_to_be_clickable(OrderPage.view_status_button))
        view_status_button.click()
