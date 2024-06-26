from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    url = "https://demo.prestashop.com/#/en/front"

    logo = (By.ID, "logo")
    start_button = (By.CLASS_NAME, "btn-download")
    explore_button = (By.CLASS_NAME, "btn-explore")
    loader = (By.ID, "loadingMessage")
    sign_out_button = (By.CLASS_NAME, "logout hidden-sm-down")
    sign_in_button = (By.CLASS_NAME, "user-info")


