import allure
from data import orders

import time
import pytest
from selenium import webdriver
from locators.order_page_locators import OrderPageLocators

class TestOrderPage:
    
    @allure.title('Заказ самоката')
    @allure.description('Нужно проверить весь флоу позитивного сценария с двумя наборами данных. Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу')
    def test_order_top(self,main_page, order_page, driver):
        main_page.close_cookie_window()
        main_page.click_top_order_button()
        # order_page.go_to_url('https://qa-scooter.praktikum-services.ru/order')
        order_page.fill_order_data_first(orders[0])
        order_page.click_next_button()
        order_page.fill_order_data_second(orders[0])
        order_page.click_order_button()
