import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    
    @allure.step('Закрываем окно с куками')
    def close_cookie_window(self):
        self.click_to_element(MainPageLocators.COOCKIE_CLOSE_BUTTON)

    @allure.step('Кликаем на вопрос {num}')
    def click_to_question(self, num):
        locators_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_LAST)
        self.click_to_element(locators_q_formatted)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, num):
        locators_q_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locators_q_formatted)
    
    @allure.step('Проверяем соответствие ответов')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)
    
    @allure.step('Открываем страницу заказа через кнопку сверху')
    def click_top_order_button(self):
        self.click_to_element(MainPageLocators.ORDER_TOP_BUTTON)
