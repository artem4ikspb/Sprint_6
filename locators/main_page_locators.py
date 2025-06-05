from selenium.webdriver.common.by import By


class MainPageLocators:
    COOCKIE_CLOSE_BUTTON = By.CSS_SELECTOR, 'button.App_CookieButton__3cvqF'
    
    QUESTION_LOCATOR = By.XPATH, './/div[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, './/div[@id="accordion__panel-{}"]'
    QUESTION_LOCATOR_LAST = By.XPATH, './/div[@id="accordion__heading-7"]'

    FAQ_MENU = (By.CSS_SELECTOR, "div.Home_FourPart__1uthg")
    YANDEX_LOGO =(By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    YANDEX_POP_UP = (By.CSS_SELECTOR, ".yc7d11a87")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")

    ORDER_TOP_BUTTON = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g")
    ORDER_BOTTOM_BUTTON = (By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm button.Button_Button__ra12g")