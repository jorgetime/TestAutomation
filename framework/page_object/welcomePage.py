from framework.page_object.base_pages.baseWebPage import BaseWebPage
from selenium.webdriver.common.by import By
from .logInPage import LogInPage


class WelcomePage(BaseWebPage):
    url = "https://www.hudl.com"
    LOG_IN_BUTTON = (By.XPATH, '//*[@class="mobile-nav-only"]/a[@href="/login"]')

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def click_log_in_button(self):
        self.click(self.LOG_IN_BUTTON, max_retry=5)
        return LogInPage(self.driver)






