from selenium.webdriver.common.by import By


class BasePageLocators:
    # Локатор для логотипа "Яндекс"
    yandex_logo = (By.CSS_SELECTOR, 'img[alt="Yandex"]')

    # Локатор для логотипа "Самокат"
    scooter_logo = (By.CSS_SELECTOR, 'a.Header_LogoScooter__3lsAR img[alt="Scooter"]')

    # Кнопка Заказать вверху страницы
    top_order_button = (By.XPATH,
                        "//div[contains(@class, 'Header_Nav__AGCXC')]//"
                        "button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
