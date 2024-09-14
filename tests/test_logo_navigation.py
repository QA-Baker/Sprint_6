from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from config import BASE_URL, DZEN_URL
import allure


@allure.title("Проверка перехода на главную страницу Самоката по клику на логотип")
@allure.description("Тест проверяет переход на главную страницу «Самоката» при нажатии на логотип «Самоката».")
def test_scooter_logo_navigation(main_page):

    base_page = BasePage(main_page)

    with allure.step("Клик по кнопке заказа"):
        order_button = WebDriverWait(main_page, 3).until(
            ec.element_to_be_clickable(BasePageLocators.top_order_button)
        )
        order_button.click()

    with allure.step("Клик по логотипу Самоката"):
        base_page.click_scooter_logo()

    with allure.step("Проверка URL главной страницы Самоката"):
        assert main_page.current_url == BASE_URL, \
            "Не произошло перехода на главную страницу Самоката."


@allure.title("Проверка перехода на главную страницу Дзена по клику на логотип Яндекса")
@allure.description("Тест проверяет переход на главную страницу Дзена при нажатии на логотип Яндекса.")
def test_yandex_logo_navigation(main_page):

    base_page = BasePage(main_page)

    with allure.step("Клик по логотипу Яндекса"):
        base_page.click_yandex_logo()

    with allure.step("Ожидание открытия новой вкладки и переключение на нее"):
        WebDriverWait(main_page, 3).until(lambda d: len(d.window_handles) > 1)
        new_window = main_page.window_handles[-1]
        main_page.switch_to.window(new_window)

    with allure.step("Проверка URL главной страницы Дзена"):
        WebDriverWait(main_page, 3).until(
            ec.url_to_be(DZEN_URL)
        )
    assert main_page.current_url == DZEN_URL, \
        "Не произошло перехода на главную страницу Дзена."
