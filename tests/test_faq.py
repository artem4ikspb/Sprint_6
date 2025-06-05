import allure
import pytest
import data

class TestFaqOnMainPage:

    @allure.title('Проверка FAQ')
    @allure.description("Тест проверяет наличие и правильность содержания вопросов и ответов")
    @allure.link(data.BASE_URL)
    @pytest.mark.parametrize(
       'num',
       [0,1,2,3,4,5,6,7]
    )
    def test_faq(self, main_page, num):
      main_page.close_cookie_window()
      assert data.answers[num] == main_page.check_question_and_answer(num)