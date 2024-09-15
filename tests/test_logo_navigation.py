import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators
from config import BASE_URL, DZEN_URL
from page_objects.main_page import MainPageMethods


@pytest.mark.usefixtures("main_page")
class TestLogoNavigation:

    @allure.title("Проверка перехода на главную страницу Самоката по клику на логотип")
    @allure.description("Тест проверяет переход на главную страницу «Самоката» при нажатии на логотип «Самоката».")
    def test_scooter_logo_navigation(self, main_page):
        main_page_methods = MainPageMethods(main_page)

        with allure.step("Клик по кнопке заказа"):
            main_page_methods.wait_until_element_clickable(BasePageLocators.top_order_button).click()

        with allure.step("Клик по логотипу Самоката"):
            main_page_methods.click_scooter_logo()

        with allure.step("Проверка URL главной страницы Самоката"):
            assert main_page_methods.get_current_url() == BASE_URL, \
                "Не произошло перехода на главную страницу Самоката."

    @allure.title("Проверка перехода на главную страницу Дзена по клику на логотип Яндекса")
    @allure.description("Тест проверяет переход на главную страницу Дзена при нажатии на логотип Яндекса.")
    def test_yandex_logo_navigation(self, main_page):
        main_page_methods = MainPageMethods(main_page)

        with allure.step("Клик по логотипу Яндекса"):
            main_page_methods.click_yandex_logo()

        with allure.step("Ожидание открытия новой вкладки и переключение на нее"):
            WebDriverWait(main_page, 5).until(lambda d: len(d.window_handles) > 1)  # Ожидаем появления новой вкладки
            new_window = main_page.window_handles[-1]
            main_page.switch_to.window(new_window)

        with allure.step("Проверка URL главной страницы Дзена"):
            WebDriverWait(main_page, 5).until(lambda d: d.current_url == DZEN_URL)
            assert main_page_methods.get_current_url() == DZEN_URL, \
                "Не произошло перехода на главную страницу Дзена."
