from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from framework.page_object.base_pages.hudlBasePage import BaseWebPage
from selenium.webdriver.common.by import By

class LogInPage(BaseWebPage):
    url = "https://www.hudl.com/login"
    EMAIL_FIELD = (By.XPATH, '//*[@id="email"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
    LOG_IN_BUTTON = (By.XPATH, '//*[@id="logIn"]')
    LOGIN_ERROR_CONTAINER = (By.XPATH, '//*[@class="login-error-container"]/p')
    LOGIN_HELP_INFO_TEXT = (By.XPATH, '//*[@class="reset-info"]/h1[contains(text(), "Login Help")]')
    NEED_HELP = (By.XPATH, '//*[@id="forgot-password-link"]')
    BACK_TO_LOGIN = (By.XPATH, '//*[@class="reset-container"]//*[@id="back-to-login"]')


    def __init__(self, driver):
        super().__init__(driver, self.url)

    def type_email(self, email):
        self.clear(self.EMAIL_FIELD)
        self.type(self.EMAIL_FIELD, email)
        return self

    def type_password(self, password):
        self.clear(self.PASSWORD_FIELD)
        self.type(self.PASSWORD_FIELD, password)
        return self

    def click_log_in_button(self):
        self.click(self.LOG_IN_BUTTON, max_retry=5)
        return self

    def click_need_help(self):
        self.click(self.NEED_HELP, max_retry=5)
        return self

    def click_back_to_login(self):
        self.click(self.BACK_TO_LOGIN, max_retry=5)
        return self

    def is_login_error_container_message_visible(self):
        return self.is_element_visible(self.LOGIN_ERROR_CONTAINER)

    def is_login_help_visible(self):
        return self.is_element_visible(self.LOGIN_HELP_INFO_TEXT)

    def is_login_button_visible(self):
            return self.is_element_visible(self.LOG_IN_BUTTON)




