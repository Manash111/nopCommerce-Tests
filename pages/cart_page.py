from basePage.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import locators


class CartPage(BasePage):

    def add_to_cart(self, index=0):
        """Adds product to cart based on its index number"""
        products = self.wait.until(
            EC.presence_of_all_elements_located(locators.btn_addToCart)
        )
        initial_count = self.get_cart_quantity()
        print(initial_count)
        products[index].click()
        return self.verify_cart_updated(initial_count)

    def get_cart_quantity(self):
        """Extracts numeric value from cart counter (e.g., '(5)' → 5)"""
        text = self.wait.until(
            EC.visibility_of_element_located(locators.cart_quantity)
        ).text
        return int(text.strip('()'))  # Remove parentheses and convert to int

    def verify_cart_updated(self, initial_count):
        """Waits for cart count to increment by 1"""
        try:
            self.wait.until(
                lambda _: self.get_cart_quantity() == initial_count + 1
            )
            return True
        except:
            return False

    def goto_cart(self):
        click_cart = self.wait.until(
            EC.visibility_of_element_located(locators.btn_shopping_cart_popup)
        )
        click_cart.click()

    def remove_product_from_cart(self,index):
        """Removes product from cart and verifies cart is empty"""

        # Get initial count (optional - for logging)
        initial_count = self.get_cart_quantity()
        print(f"Initial cart items: {initial_count}")

        # Remove product
        remove_product = self.wait.until(
            EC.presence_of_all_elements_located(locators.btn_remove_product)
        )
        remove_product[index].click()

        # Verification
        return self._verify_cart_empty()

    def _verify_cart_empty(self):
        """Verifies cart is empty through multiple checks"""
        try:
            # Check counter shows (0)
            self.wait.until(
                lambda _: self.get_cart_quantity() == 0
            )

            assert "Your Shopping Cart is empty!" in self.driver.page_source
            return True
        except Exception as e:
            print(f"Cart empty verification failed: {str(e)}")
            return False