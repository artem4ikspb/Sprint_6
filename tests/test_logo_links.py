import allure

class TestLogoLinks:

    @allure.title('Проверка перехода по клику на лого самоката')
    @allure.description('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_click_scooter_logo(self, main_page):
        main_page.click_scooter_logo()
        assert main_page.is_main_page_visible()

    @allure.title('Проверка перехода по клику на Ya лого')
    @allure.description('Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def test_click_ya_logo(self, main_page):
        main_page.click_ya_logo()
        assert main_page.is_dzen_loaded()

    
