import pytest
import allure
from page_objects.order_page import OrderPageMethods
from test_data import order_test_data


@pytest.mark.usefixtures("main_page")
class TestOrderPage:

    @allure.title("Позитивный сценарий заказа самоката через разные точки входа")
    @allure.description("Тест проверяет оформление заказа самоката через две точки входа и с разными наборами данных.")
    @pytest.mark.parametrize("entry_point, order_data", order_test_data)
    def test_order_flow(self, main_page, entry_point, order_data):
        order_page_methods = OrderPageMethods(main_page)  # Создание объекта в тесте

        with allure.step("Ожидание кликабельности кнопки входа в заказ и переход к форме заказа"):
            entry_button = order_page_methods.wait_until_element_clickable(entry_point)
            order_page_methods.execute_script("arguments[0].click();", entry_button)

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
            assert order_page_methods.is_view_status_button_visible(), \
                "Кнопка 'Посмотреть статус' не отображается после оформления заказа."
