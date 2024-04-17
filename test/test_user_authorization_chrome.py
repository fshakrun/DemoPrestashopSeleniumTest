import allure

from pages.main_page import MainPage
from pages.log_in_form_page import LogInPage


class TestUserAuth:

    @allure.title("Wrong Credential Authentification Failed Test")
    def test_invalid_creds(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(main_page.url)
        main_page.switch_to_frame("framelive")
        main_page.find_element(main_page.sign_in_button).click()
        log_in_form_page = LogInPage(driver)
        log_in_form_page.submit_login_form()
        alert = log_in_form_page.find_element(log_in_form_page.alert_message)
        assert alert.text == "Authentication failed."

    @allure.title("Password Recovery Test")
    def test_password_recovery(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(main_page.url)
        main_page.switch_to_frame("framelive")
        main_page.find_element(main_page.sign_in_button).click()
        log_in_form_page = LogInPage(driver)
        log_in_form_page.recover_password()
        recover_success = log_in_form_page.find_element(log_in_form_page.recovery_message)
        assert recover_success.is_displayed()