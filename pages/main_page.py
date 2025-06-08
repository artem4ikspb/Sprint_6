import allure
from locators.general_locators import GeneralLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

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

    @allure.step('Открываем страницу заказа через кнопку снизу')
    def click_bottom_order_button(self):
        self.click_to_element(MainPageLocators.ORDER_BOTTOM_BUTTON)

    @allure.step('Кликаем по Yandex логотипу в хедере')
    def click_ya_logo(self):
        self.click_to_element(GeneralLocators.YA_LOGO)

    @allure.step('Кликаем по логотипу скутера в хедере')
    def click_scooter_logo(self):
        self.click_to_element(GeneralLocators.SCOOTER_LOGO)

    @allure.step('Закрываем окно с куками')
    def close_cookie_window(self):
        self.click_to_element(GeneralLocators.COOCKIE_CLOSE_BUTTON)

    @allure.step('Проверяем что главная страница загрузилась')
    def is_main_page_visible(self):
        return self.is_visible(MainPageLocators.MAIN_PAGE_LOCATOR)
    
    @allure.step('Убедимся что страница заказов загрузилась')
    def is_order_page_visible(self):
        return self.is_visible(OrderPageLocators.ORDER_PAGE_HEADER)
    
    @allure.step('Проверяем что страница Dzen загрузился')
    def is_dzen_loaded(self):
        self.switch_to_new_tab()
        return self.is_visible(GeneralLocators.DZEN_HEADER)