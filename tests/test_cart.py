import time
import unittest
import locators
from base_test import BaseTest
from pages.search_page import SearchPage
from pages.cart_page import CartPage

class TestCart(BaseTest):

    def test_add_to_cart(self):
        self.driver.get(locators.base_url)

        search = SearchPage(self.driver)
        cart = CartPage(self.driver)

        search_product = "Laptop"
        product_index = 1
        search.search(search_product)
        is_updated = cart.add_to_cart(product_index)
        self.assertTrue(
            is_updated,
            f"Cart count did not update after adding {search_product} (index: {product_index})"
        )

        print(f"Current cart items: {cart.get_cart_quantity()}")