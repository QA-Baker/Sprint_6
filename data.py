from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators

faq_test_data = [
    (MainPageLocators.price_and_payment, MainPageLocators.price_info),
    (MainPageLocators.multiple_scooters, MainPageLocators.multiple_scooters_info),
    (MainPageLocators.rental_time_calculation, MainPageLocators.rental_time_info),
    (MainPageLocators.order_today, MainPageLocators.order_today_info),
    (MainPageLocators.extend_or_return, MainPageLocators.extend_or_return_info),
    (MainPageLocators.charger_included, MainPageLocators.charger_included_info),
    (MainPageLocators.cancel_order, MainPageLocators.cancel_order_info),
    (MainPageLocators.outside_mkad, MainPageLocators.outside_mkad_info),
]
order_test_data = [
    (BasePageLocators.top_order_button, {
        "first_name": "Иван",
        "last_name": "Иванов",
        "address": "Москва, ул. Арбат, д. 12",
        "metro_station": "Арбатская",
        "phone_number": "+79991234567",
        "rent_date": "01.05.2025",
        "rent_term": "двое суток",
        "color": "black",
        "comment": "Позвонить за час до доставки"
    }),
    (BasePageLocators.bottom_order_button, {
        "first_name": "Анна",
        "last_name": "Петрова",
        "address": "Москва, Тверская ул., д. 5",
        "metro_station": "Тверская",
        "phone_number": "+79997654321",
        "rent_date": "01.07.2025",
        "rent_term": "сутки",
        "color": "grey",
        "comment": "Не звонить, просто оставить у двери"
    })
]
