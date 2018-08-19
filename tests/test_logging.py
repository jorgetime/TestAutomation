from framework.page_object.welcomePage import WelcomePage


def test_logging_user_can_login(given_a_user_just_logged_in):
    home_page = given_a_user_just_logged_in

    assert home_page.get_coach_name() == 'Coach Onuoha'


def test_logging_error(given_a_browser):
    driver = given_a_browser
    welcome_page = WelcomePage(driver)
    log_in_page = welcome_page.click_log_in_button()
    log_in_page.type_email('jorgeonuohacid@gmail.com') \
        .type_password('incorrect password') \
        .click_log_in_button()
    assert log_in_page.is_login_error_container_message_visible()


def test_logging_need_help(given_a_browser):
    driver = given_a_browser
    log_in_page = WelcomePage(driver).click_log_in_button()
    log_in_page.click_need_help()
    assert log_in_page.is_login_help_visible()

    log_in_page.click_back_to_login()
    assert log_in_page.is_login_button_visible()

# Other scenario
def test_logging_remember_me_flow():
    # Test for functionality of 'remember me' button
    pass



