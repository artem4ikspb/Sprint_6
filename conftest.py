import data
import pytest
from pages.main_page import MainPage
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 1024)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(data.URL_MAIN_PAGE)
    return page
    