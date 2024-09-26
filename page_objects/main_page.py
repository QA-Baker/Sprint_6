from page_objects.base_page import BasePage


class MainPage(BasePage):

    def click_faq_question(self, locator):
        self.click_element(locator)

    def check_faq_answer_displayed(self, locator):
        element = self.find_element(locator)
        return element.is_displayed()
