import logging
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions


class BaseWebPage(object):
    logger = logging.getLogger('test')

    def __init__(self, driver, url):
        self.driver = driver
        if driver.current_url is not url:
            self.driver.get(url)

    def find_element(self, locator):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return element

    def clear(self, locator):
        self.find_element(locator)\
            .clear()
        return self

    def type(self, locator, text):
        self.find_element(locator)\
            .send_keys(text)
        return self

    def click(self, locator, max_retry=2):
        retry = 0
        while(retry < max_retry):
            try:
                element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
                element.click()
                return self
            except (exceptions.WebDriverException, exceptions.StaleElementReferenceException) as ex:
                if retry >= max_retry:
                    self.logger.error("Locator not found")
                self.logger.warning("Locator cannot be clicker (retry {})".format(retry))
                retry += 1
                sleep(1)

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10)\
                .until(expected_conditions.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
