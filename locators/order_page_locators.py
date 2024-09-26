from selenium.webdriver.common.by import By


class OrderPage:
    # Локаторы для полей ввода данных о том, кто арендует самокат
    first_name_field = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z[placeholder="* Имя"]')
    last_name_field = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z[placeholder="* Фамилия"]')
    address_field = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z[placeholder="* Адрес: куда привезти заказ"]')
    metro_station_field = (By.CSS_SELECTOR, 'input.select-search__input[placeholder="* Станция метро"]')
    phone_number_field = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z[placeholder="* Телефон: на него позвонит курьер"]')

    # Локатор для кнопки "Далее"
    next_button = (By.CSS_SELECTOR, 'button.Button_Button__ra12g.Button_Middle__1CSJM')

    # Локаторы для полей ввода условий по аренде
    rent_date_field = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z[placeholder="* Когда привезти самокат"]')
    rent_term_dropdown = (By.CSS_SELECTOR, 'div.Dropdown-placeholder')

    # Локаторы для чекбоксов выбора цвета самоката
    scooter_color_black = (By.CSS_SELECTOR, 'input.Checkbox_Input__14A2w#black')
    scooter_color_grey = (By.CSS_SELECTOR, 'input.Checkbox_Input__14A2w#grey')

    # Локатор для поля с комментарием курьеру
    courier_comment_field = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z[placeholder="Комментарий для курьера"]')

    # Локатор для кнопки Заказать
    middle_order_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') "
                                     "and contains(text(), 'Заказать')]")

    # Локатор для кнопки "Да" в модальном окне подтверждения заказа
    confirm_order_button = (By.XPATH, '//button[text()="Да" and @class="Button_Button__ra12g Button_Middle__1CSJM"]')

    # Локатор для кнопки "Посмотреть статус" после оформления заказа
    view_status_button = (
        By.XPATH, '//button[text()="Посмотреть статус" and @class="Button_Button__ra12g Button_Middle__1CSJM"]')

    # Дополнительные локаторы
    rent_term_option_template = ('//div[@class="Dropdown-option" and text()="{term}"]', By.XPATH)
    metro_option_template = ('//div[contains(@class, "select-search__select")]//*[text()="{metro_name}"]', By.XPATH)
