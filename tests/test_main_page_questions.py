import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_data import faq_test_data
import allure


@allure.title("Проверка раскрытия вопросов в разделе FAQ")
@allure.description("Тест проверяет, что при нажатии на вопрос в разделе FAQ раскрывается правильный текст.")
@pytest.mark.parametrize("question_locator, answer_locator", faq_test_data)
def test_faq_expand(main_page, question_locator, answer_locator):
    with allure.step(f"Ожидание кликабельности вопроса {question_locator}"):
        question_element = WebDriverWait(main_page, 3).until(
            ec.element_to_be_clickable(question_locator)
        )

    with allure.step("Клик по вопросу"):
        main_page.execute_script("arguments[0].click();", question_element)

    with allure.step(f"Ожидание отображения ответа на вопрос {question_locator}"):
        answer_element = WebDriverWait(main_page, 3).until(
            ec.visibility_of_element_located(answer_locator)
        )

    with allure.step(f"Проверка, что ответ {answer_locator} отображается"):
        assert answer_element.is_displayed(), f"Ответ на вопрос {question_locator} не отображается."
