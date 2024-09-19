import pytest
import allure
from page_objects.base_page import BasePage
from config import BASE_URL, DZEN_URL


@pytest.mark.usefixtures("main_page")
class TestLogoNavigation:

    @allure.title("Проверка перехода на главную страницу Самоката по клику на логотип")
    @allure.description("Тест проверяет переход на главную страницу «Самоката» при нажатии на логотип «Самоката».")
    def test_scooter_logo_navigation(self, main_page):
        base_page = BasePage(main_page)

        with allure.step("Клик по логотипу Самоката"):
            base_page.click_scooter_logo()

        with allure.step("Проверка URL главной страницы Самоката"):
            assert base_page.get_current_url() == BASE_URL, \
                "Не произошло перехода на главную страницу Самоката."

    @allure.title("Проверка перехода на главную страницу Дзена по клику на логотип Яндекса")
    @allure.description("Тест проверяет переход на главную страницу Дзена при нажатии на логотип Яндекса.")
    def test_yandex_logo_navigation(self, main_page):
        base_page = BasePage(main_page)

        with allure.step("Клик по логотипу Яндекса"):
            base_page.click_yandex_logo()

        with allure.step("Ожидание открытия новой вкладки"):
            base_page.wait_for_new_tab()

        with allure.step("Переключение на новую вкладку"):
            base_page.switch_to_new_tab()

        with allure.step("Ожидание загрузки страницы в новой вкладке"):
            base_page.wait_for_url_to_be(DZEN_URL)

        with allure.step("Проверка URL главной страницы Дзена"):
            assert base_page.get_current_url() == DZEN_URL, \
                "Не произошло перехода на главную страницу Дзена."
