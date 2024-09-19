import pytest
import allure
from test_data import order_test_data


@pytest.mark.usefixtures("main_page")
class TestOrderPage:

    @allure.title("Позитивный сценарий заказа самоката через разные точки входа")
    @allure.description("Тест проверяет оформление заказа самоката через две точки входа и с разными наборами данных.")
    @pytest.mark.parametrize("entry_point, order_data", order_test_data)
    def test_order_flow(self, order_page, entry_point, order_data):
        with allure.step("Ожидание кликабельности кнопки входа в заказ и переход к форме заказа"):
            order_page.click_element_with_js(entry_point)

        with allure.step("Заполнение формы заказа"):
            order_page.input_first_name(order_data["first_name"])
            order_page.input_last_name(order_data["last_name"])
            order_page.input_address(order_data["address"])
            order_page.select_metro_station(order_data["metro_station"])
            order_page.input_phone_number(order_data["phone_number"])
            order_page.click_next_button()

        with allure.step("Заполнение данных аренды"):
            order_page.input_rent_date(order_data["rent_date"])
            order_page.select_rent_term(order_data["rent_term"])
            order_page.select_scooter_color(order_data["color"])
            order_page.input_courier_comment(order_data["comment"])

        with allure.step("Подтверждение и завершение оформления заказа"):
            order_page.click_middle_order_button()
            order_page.click_confirm_order_button()

        with allure.step("Проверка появления кнопки 'Посмотреть статус'"):
            assert order_page.is_view_status_button_visible(), \
                "Кнопка 'Посмотреть статус' не отображается после оформления заказа."
