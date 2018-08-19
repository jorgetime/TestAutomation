from selenium.webdriver.common.by import By
from framework.page_object.base_pages.hudlBasePage import HudlBasePage


class HomePage(HudlBasePage):
    url = "https://www.hudl.com/home"
    COACH_DISPLAY_NAME = (By.XPATH, '//*[@class="hui-globaluseritem__display-name"]/span')


    def get_coach_name(self):
        element = self.find_element(self.COACH_DISPLAY_NAME)
        return element.get_attribute("innerHTML")

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def click_on_feed(self):
        pass

    def click_on_trending(self):
        pass

    def click_on_featured(self):
        pass
