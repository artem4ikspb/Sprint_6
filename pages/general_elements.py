import allure
from locators.general_locators import GeneralLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class GeneralElements(BasePage):
    
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