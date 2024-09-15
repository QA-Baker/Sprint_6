import pytest
import allure
from test_data import faq_test_data
from page_objects.main_page import MainPageMethods


@pytest.mark.usefixtures("main_page")
class TestMainPageQuestions:

    @allure.title("Проверка раскрытия вопросов в разделе FAQ")
    @allure.description("Тест проверяет, что при нажатии на вопрос в разделе FAQ раскрывается правильный текст.")
    @pytest.mark.parametrize("question_locator, answer_locator", faq_test_data)
    def test_faq_expand(self, main_page, question_locator, answer_locator):
        main_page_methods = MainPageMethods(main_page)

        with allure.step(f"Ожидание кликабельности вопроса {question_locator}"):
            question_element = main_page_methods.wait_until_element_clickable(question_locator)

        with allure.step("Клик по вопросу"):
            main_page_methods.execute_script("arguments[0].click();", question_element)

        with allure.step(f"Ожидание отображения ответа на вопрос {question_locator}"):
            answer_element = main_page_methods.wait_until_element_visible(answer_locator)

        with allure.step(f"Проверка, что ответ {answer_locator} отображается"):
            assert answer_element.is_displayed(), f"Ответ на вопрос {question_locator} не отображается."
