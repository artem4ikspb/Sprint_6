import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открываем страницу {url}')
    def go_to_url(self, url):
        return self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def click_to_element(self, locator):
        self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )
        return self.driver.find_element(*locator).click()
    
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def add_date_to_element(self, locator, date):
        self.find_element_with_wait(locator).send_keys(date)
        self.find_element_with_wait(locator).send_keys(Keys.ENTER)


    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    def format_locators(self, locator, num):
        method, locator_formatted = locator
        locator_formatted = locator_formatted.format(num)
        return (method, locator_formatted)
    
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator) 
        self.driver.execute_script("arguments[0].scrollIntoView();", element)