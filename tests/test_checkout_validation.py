import time
import unittest
from basePage.base_test import BaseTest
from pages.checkout_page import CheckoutPage
import locators
from pages.search_page import SearchPage
from pages.cart_page import CartPage

class TestCheckoutValidation(BaseTest):
    def test_empty_field_validation(self):

        # goto url
        self.driver.get(locators.base_url)

        # initialize
        search_page = SearchPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        # search product and add to cart
        product = "iPhone"
        search_page.search(product)
        cart_page.add_to_cart(0)  # Add first search result
        cart_page.goto_cart()
        checkout_page.start_guest_checkout()
        checkout_page.continue_with_no_details()
        checkout_page.close_alert()




if __name__ == "__main__":
    unittest.main()