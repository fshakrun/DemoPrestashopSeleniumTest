import allure

from pages.main_page import MainPage


class TestShopAccess:

    @allure.title("Online Shop Availablility Test")
    def test_online_shop_is_opened(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(main_page.url)
        main_page.switch_to_frame("framelive")
        page_title = driver.title
        expected_title = "PrestaShop Live Demo"
        assert page_title == expected_title
