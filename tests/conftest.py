import pytest
from selenium import webdriver
from framework.page_object.homePage import HomePage
from framework.page_object.welcomePage import WelcomePage
from selenium.webdriver.support import  expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import os


@pytest.fixture()
def given_a_browser():
    chrome_path = os.path.dirname(os.path.abspath(__file__)).rsplit("test", 1)[0] \
                  + "framework\\driver\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    return driver

@pytest.fixture()
def given_a_user_just_logged_in(given_a_browser):
    driver = given_a_browser
    welcome_page = WelcomePage(driver)
    log_in_page = welcome_page.click_log_in_button()
    log_in_page.type_email('jorgeonuohacid@gmail.com') \
        .type_password('InstantR68') \
        .click_log_in_button()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(HomePage.COACH_DISPLAY_NAME))

    return HomePage(driver)