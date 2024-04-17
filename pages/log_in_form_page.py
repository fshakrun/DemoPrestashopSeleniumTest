from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LogInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    url = "https://demo.prestashop.com/#/en/front"

    loader = (By.XPATH, "//*[@id='loadingMessage']/img")
    sign_in_link = (By.CLASS_NAME, "user-info")
    email_input = (By.ID, "field-email")
    password_input = (By.ID, "field-password")
    submit_btn = (By.XPATH, "//button[@type='submit']")
    alert_message = (By.CLASS_NAME, "alert-danger")
    forgot_password_button = (By.XPATH, "//*[@id='login-form']/div/div[3]/a")
    recover_pass_emailfield = (By.XPATH, "//*[@id='email']")
    reset_pass_link_button = (By.XPATH, "//*[@id='send-reset-link']")
    recovery_message = (By.XPATH, "//*[@id='content']/ul/li/p")

    def submit_login_form(self):
        self.find_element(self.email_input).send_keys("wrongcredentialstest@test.com")
        self.find_element(self.password_input).send_keys("justfortesting")
        self.find_element(self.submit_btn).click()

    def alert_message_present(self):
        self.find_element(self.alert_message)

    def recover_password(self):
        self.find_element(self.forgot_password_button).click()
        self.find_element(self.recover_pass_emailfield).click()
        self.find_element(self.recover_pass_emailfield).send_keys("wrongcredentialstest@test.com")
        self.find_element(self.reset_pass_link_button).click()

    def recovery_message_present(self):
        self.find_element(self.recovery_message)
