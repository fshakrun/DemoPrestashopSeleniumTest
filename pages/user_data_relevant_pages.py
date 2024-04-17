from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserDataPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    url = "https://demo.prestashop.com/#/en/front"

    personal_infos_form = (By.XPATH, "//*[@id='checkout-personal-information-step']/h1")
    social_title = (By.XPATH, "//*[@id='field-id_gender-1']")
    name_field = (By.ID, "field-firstname")
    lastname_field = (By.ID, "field-lastname")
    email_field = (By.ID, "field-email")
    password_field = (By.ID, "field-password")
    agree_checkbox = (By.XPATH, "//*[@id='customer-form']/div/div[8]/div[1]/span")
    customer_data_checkbox = (By.XPATH, "//*[@id='customer-form']/div/div[10]/div[1]/span")
    data_privacy_checkbox = (By.CSS_SELECTOR, 'input[name="customer_privacy"]')
    continue_button = (By.CSS_SELECTOR, ".btn.btn-primary.float-xs-right")
    confirm_adress_btn = (By.XPATH, "//*[@id='delivery-address']/div/footer/button")
    shipping_method_btn = (By.XPATH, "//*[@id='js-delivery']/button")
    submit_button = (By.CLASS_NAME, 'form-control-submit')
    log_in_text = (By.XPATH, '//h1[contains(text(), "Log in")]')
    new_account = (By.CSS_SELECTOR, ".no-account > a")
    sign_out_button = (By.CSS_SELECTOR, ".user-info > a")
    address_field = (By.XPATH, "//*[@id='field-address1']")
    zip_code = (By.XPATH, "//*[@id='field-postcode']")
    city_name = (By.XPATH, "//*[@id='field-city']")
    delivery_button = (By.XPATH, "//*[@id='js-delivery']/button")
    bank_wire_selecting = (By.XPATH, "//*[@id='payment-option-1']")
    adreed_therms = (By.XPATH, "//*[@id='conditions_to_approve[terms-and-conditions]']")
    place_order_btn = (By.XPATH, "//*[@id='payment-confirmation']/div[1]/button")
    order_placing_message = (By.XPATH, "//*[@id='content-hook_order_confirmation']/div/div/div/h3")

    def submit_order_infos(self):
        self.wait_element_present(self.personal_infos_form, 120)
        self.find_element(self.social_title).click()
        self.find_element(self.name_field).send_keys("Antonin")
        self.find_element(self.lastname_field).send_keys("Artaud")
        self.find_element(self.email_field).send_keys("anartaud@fortest.net")
        self.find_element(self.agree_checkbox).click()
        self.find_element(self.customer_data_checkbox).click()
        self.find_element(self.continue_button).click()
        self.find_element(self.address_field).send_keys("31 rue de Gagarin")
        self.find_element(self.zip_code).send_keys("75000")
        self.find_element(self.city_name).send_keys("Cergy")
        self.find_element(self.confirm_adress_btn).click()
        self.find_element(self.shipping_method_btn).click()
        self.find_element(self.bank_wire_selecting).click()
        self.find_element(self.adreed_therms).click()
        self.find_element(self.place_order_btn).click()
        self.wait_element_present(self.order_placing_message, 120)
