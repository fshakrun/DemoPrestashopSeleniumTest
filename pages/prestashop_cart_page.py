from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from test.conftest import driver


class PrestashopCart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    item_add = (By.CSS_SELECTOR, "#content > section:nth-child(2) > div > div:nth-child(1)")
    add_to_cart = (By.XPATH, "//button[@type='submit']")
    add_to_cart_button = (By.XPATH, "//button[@type='submit']")
    proceed_to_basket_btn = (By.XPATH, "//button[@type='button']")
    really_proceed_to_checkout = (By.CSS_SELECTOR, ".btn.btn-primary")
    pop_up = (By.XPATH, "//*[@id='blockcart-modal']/div/div")
    go_to_cart = (By.CSS_SELECTOR, "#_desktop_cart > div > div")
    shop_logo = (By.CSS_SELECTOR, ".logo.img-fluid")
    cart_go = (By.XPATH, "//span[text()='Cart']")
    final_proceed_checkout = (By.CSS_SELECTOR, ".btn.btn-primary")
    search_in_catalog = (By.XPATH, "//*[@id='search_widget']/form/input[2]")
    first_item_in_search_result = (By.XPATH, "//*[@id='js-product-list']/div[1]/div[1]/article/div/div[2]/h2")

    def add_item_in_my_cart(self, driver):
        self.find_element(self.item_add).click()
        self.find_element(self.add_to_cart).click()
        self.wait_element_present(self.pop_up)
        actions = ActionChains(driver)
        actions.move_by_offset(800, 600).double_click().perform()
        actions.reset_actions()

    def proceed_in_my_cart(self):
        self.wait_element_present(self.go_to_cart)
        self.find_element(self.go_to_cart).click()
        self.find_element(self.final_proceed_checkout).click()

    def item_search(self):
        self.wait_element_present(self.search_in_catalog)
        self.find_element(self.search_in_catalog).click()
        self.find_element(self.search_in_catalog).send_keys("Mug")
        self.find_element(self.search_in_catalog).send_keys(u'\ue007')
