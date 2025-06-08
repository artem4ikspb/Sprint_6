from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_LOCATOR = By.CSS_SELECTOR, 'div.Home_FirstPart__3g6vG'    
    QUESTION_LOCATOR = By.XPATH, './/div[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, './/div[@id="accordion__panel-{}"]'
    QUESTION_LOCATOR_LAST = By.XPATH, './/div[@id="accordion__heading-7"]'

    FAQ_MENU = By.CSS_SELECTOR, "div.Home_FourPart__1uthg"
    SCOOTER_LOGO = By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR"

    ORDER_TOP_BUTTON = By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g"
    ORDER_BOTTOM_BUTTON = By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm button.Button_Button__ra12g"
