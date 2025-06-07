import allure
import pytest
from data import orders


class TestOrderPage:
 
    @allure.title('Проверка верхней кнопки перехода на страницу заказа')
    def test_top_order_button(self, main_page):
        main_page.close_cookie_window()
        main_page.click_top_order_button()
        assert main_page.is_order_page_visible()

    @allure.title('Проверка нижней кнопки перехода на страницу заказа')
    def test_bottom_order_button(self, main_page):
        main_page.close_cookie_window()
        main_page.click_bottom_order_button()
        assert main_page.is_order_page_visible()

    @allure.title('Заказа самоката')
    @allure.description('Нужно проверить весь флоу позитивного сценария с двумя наборами данных.')
    @pytest.mark.parametrize(
       'num',
       [1]
    )
    def test_order(self, order_page, num):
        order_page.fill_order_data_first(orders[num])
        order_page.click_next_button()
        order_page.fill_order_data_second(orders[num])
        order_page.click_order_button()
        order_page.confirm_order()
        assert order_page.check_modal_order('Заказ оформлен')
