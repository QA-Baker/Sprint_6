from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    # Метод для поиска элемента
    def find_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    # Метод для клика по элементу
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    # Метод для клика по элементу через JavaScript
    def click_element_with_js(self, locator):
        element = self.find_element(locator)
        self.execute_script("arguments[0].click();", element)

    # Метод для ввода текста
    def enter_text(self, locator, text: str):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    # Выполнение JavaScript
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    # Получение текущего URL
    def get_current_url(self):
        return self.driver.current_url

    # Клики по логотипам
    def click_yandex_logo(self):
        self.click_element(BasePageLocators.yandex_logo)

    def click_scooter_logo(self):
        self.click_element(BasePageLocators.scooter_logo)

    # Ожидание открытия новой вкладки
    def wait_for_new_tab(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)

    # Переключение на новую вкладку
    def switch_to_new_tab(self):
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    # Ожидание пока URL станет определённым
    def wait_for_url_to_be(self, expected_url, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.url_to_be(expected_url))
