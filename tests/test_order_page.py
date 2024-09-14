import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.order_page import OrderPageMethods
from locators.order_page_locators import OrderPage
from test_data import order_test_data
import allure


@allure.title("Позитивный сценарий заказа самоката через разные точки входа")
@allure.description("Тест проверяет оформление заказа самоката через две точки входа и с разными наборами данных.")
@pytest.mark.parametrize("entry_point, order_data", order_test_data)
def test_order_flow(main_page, entry_point, order_data):
    order_page_methods = OrderPageMethods(main_page)

    with allure.step("Ожидание кликабельности кнопки входа в заказ и переход к форме заказа"):
        entry_button = WebDriverWait(main_page, 3).until(
            ec.element_to_be_clickable(entry_point)
        )
        main_page.execute_script("arguments[0].click();", entry_button)

    with allure.step("Заполнение формы заказа"):
        order_page_methods.input_first_name(order_data["first_name"])
        order_page_methods.input_last_name(order_data["last_name"])
        order_page_methods.input_address(order_data["address"])
        order_page_methods.select_metro_station(order_data["metro_station"])
        order_page_methods.input_phone_number(order_data["phone_number"])
        order_page_methods.click_next_button()

    with allure.step("Заполнение данных аренды"):
        order_page_methods.input_rent_date(order_data["rent_date"])
        order_page_methods.select_rent_term(order_data["rent_term"])
        order_page_methods.select_scooter_color(order_data["color"])
        order_page_methods.input_courier_comment(order_data["comment"])

    with allure.step("Подтверждение и завершение оформления заказа"):
        order_page_methods.click_middle_order_button()
        order_page_methods.click_confirm_order_button()

    with allure.step("Проверка появления кнопки 'Посмотреть статус'"):
        assert WebDriverWait(main_page, 3).until(
            ec.visibility_of_element_located(OrderPage.view_status_button)
        ).is_displayed(), "Кнопка 'Посмотреть статус' не отображается после оформления заказа."
