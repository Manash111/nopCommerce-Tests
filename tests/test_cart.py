import locators
from basePage.base_test import BaseTest
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

    def test_remove_from_cart(self):

        # Initialize pages
        cart = CartPage(self.driver)
        cart.goto_cart()

        # Remove product
        is_empty = cart.remove_product_from_cart(0)
        # Assertions
        self.assertTrue(
            is_empty,
            "Cart did not empty after removal"
        )
        print("Cart successfully emptied")
