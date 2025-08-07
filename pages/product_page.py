from base_page import BasePage
import locators
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def verify_product_details(self, expected_name, expected_price):
        """Verifies core product details with assertions"""
        # Wait for elements to load
        actual_name = self.get_text(locators.product_name)
        actual_price = self.get_text(locators.product_price)

        # Verify image is loaded (not broken)
        image = self.wait.until(
            EC.presence_of_element_located(locators.product_image)
        )
        assert image.get_attribute("src") != "", "Product image is missing"

        # Verify description exists
        assert self.is_visible(locators.product_description), "Description missing"

        # Verify name and price
        assert actual_name == expected_name, f"Expected {expected_name}, got {actual_name}"
        assert actual_price == expected_price, f"Expected {expected_price}, got {actual_price}"

        return True