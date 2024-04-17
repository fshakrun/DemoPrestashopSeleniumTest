import allure

from pages.main_page import MainPage
from pages.prestashop_cart_page import PrestashopCart
from pages.user_data_relevant_pages import UserDataPage


class TestUsersPath:

    @allure.title("Placing Order Test")
    def test_placing_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(main_page.url)
        main_page.wait_element_present(main_page.logo, 60)
        main_page.switch_to_frame("framelive")
        prestashop_cart_page = PrestashopCart(driver)
        prestashop_cart_page.add_item_in_my_cart(driver)
        prestashop_cart_page.proceed_in_my_cart()
        user_data_relevant_pages = UserDataPage(driver)
        user_data_relevant_pages.submit_order_infos()
        succesfully_placed_order_message = user_data_relevant_pages.find_element(
            user_data_relevant_pages.order_placing_message)
        assert succesfully_placed_order_message.is_displayed()

    @allure.title("Searching Items Relevant Result Check")
    def test_search_items_relevant(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(main_page.url)
        main_page.wait_element_present(main_page.logo, 60)
        main_page.switch_to_frame("framelive")
        prestashop_cart_page = PrestashopCart(driver)
        prestashop_cart_page.item_search()
        first_search_result = prestashop_cart_page.find_element(prestashop_cart_page.first_item_in_search_result)
        assert "Mug" in str(first_search_result.text)
