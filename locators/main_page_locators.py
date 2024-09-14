from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы для блока Вопросы о важном
    price_and_payment = [By.XPATH, '//div[contains(text(), "Сколько это стоит? И как оплатить?")]']
    multiple_scooters = [By.XPATH, '//div[contains(text(), "Хочу сразу несколько самокатов! Так можно?")]']
    rental_time_calculation = [By.XPATH, '//div[contains(text(), "Как рассчитывается время аренды?")]']
    order_today = [By.XPATH, '//div[contains(text(), "Можно ли заказать самокат прямо на сегодня?")]']
    extend_or_return = [By.XPATH, '//div[contains(text(), "Можно ли продлить заказ или вернуть самокат раньше?")]']
    charger_included = [By.XPATH, '//div[contains(text(), "Вы привозите зарядку вместе с самокатом?")]']
    cancel_order = [By.XPATH, '//div[contains(text(), "Можно ли отменить заказ?")]']
    outside_mkad = [By.XPATH, '//div[contains(text(), "Я жизу за МКАДом, привезёте?")]']

    # Локаторы для раскрывающихся дополнительных сведений
    price_info = [By.XPATH, '//p[contains(text(), "Сутки — 400 рублей. Оплата курьеру — наличными или картой.")]']
    multiple_scooters_info = [By.XPATH,
                              '//p[contains(text(), "Пока что у нас так: один заказ — один самокат. '
                              'Если хотите покататься с друзьями,'
                              ' можете просто сделать несколько заказов — один за другим.")]']
    rental_time_info = [By.XPATH,
                        '//p[contains(text(), "Допустим, вы оформляете заказ на 8 мая. '
                        'Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, '
                        'когда вы оплатите заказ курьеру. '
                        'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")]']
    order_today_info = [By.XPATH,
                        '//p[contains(text(), "Только начиная с завтрашнего дня. Но скоро станем расторопнее.")]']
    extend_or_return_info = [By.XPATH,
                             '//p[contains(text(), "Пока что нет! '
                             'Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")]']
    charger_included_info = [By.XPATH,
                             '//p[contains(text(), "Самокат приезжает к вам с полной зарядкой. '
                             'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                             'Зарядка не понадобится.")]']
    cancel_order_info = [By.XPATH,
                         '//p[contains(text(), "Да, пока самокат не привезли. '
                         'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.")]']
    outside_mkad_info = [By.XPATH,
                         '//p[contains(text(), "Да, обязательно. Всем самокатов! И Москве, и Московской области.")]']
