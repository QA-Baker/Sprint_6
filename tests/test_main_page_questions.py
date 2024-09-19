import pytest
import allure
from test_data import faq_test_data
from page_objects.base_page import BasePage


@pytest.mark.usefixtures("main_page")
class TestMainPageQuestions:

    @allure.title("Проверка раскрытия вопросов в разделе FAQ")
    @allure.description("Тест проверяет, что при нажатии на вопрос в разделе FAQ раскрывается правильный текст.")
    @pytest.mark.parametrize("question_locator, answer_locator", faq_test_data)
    def test_faq_expand(self, main_page, question_locator, answer_locator):
        base_page = BasePage(main_page)

        with allure.step(f"Клик по вопросу {question_locator}"):
            base_page.click_element_with_js(question_locator)

        with allure.step(f"Ожидание отображения ответа на вопрос {question_locator}"):
            answer_element = base_page.find_element(answer_locator)

        with allure.step(f"Проверка, что ответ {answer_locator} отображается"):
            assert answer_element.is_displayed(), f"Ответ на вопрос {question_locator} не отображается."
