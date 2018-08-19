import logging
from selenium.webdriver.common.by import By
from framework.page_object.base_pages.baseWebPage import BaseWebPage


class HudlBasePage(BaseWebPage):
    logger = logging.getLogger('test')

    HUI_USER_DISPLAY_NAME = (By.XPATH, '//*[@class="hui-globaluseritem__display-name"]')
    LOG_OUT_BUTTON = (By.XPATH, '//*[@class="hui-globalusermenu"]//*[@data-qa-id="webnav-usermenu-logout"]')

    def __init__(self, driver, url):
        self.driver = driver
        super().__init__(driver, url)

    def log_out(self):
        self.find_element(self.HUI_USER_DISPLAY_NAME).click()
        self.find_element(self.LOG_OUT_BUTTON).click()
        return self

    def click_on_home(self):
        pass

    def click_on_explore(self):
        pass

    def click_on_video(self):
        pass

    def click_on_reports(self):
        pass

    def click_on_team_profile(self):
        pass

    def click_on_manage_team(self):
        pass

    def click_on_schedule(self):
        pass

    def click_on_highlights(self):
        pass