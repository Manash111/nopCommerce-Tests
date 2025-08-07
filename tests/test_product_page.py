import unittest

import locators
from base_test import BaseTest
from pages.product_page import ProductPage
from pages.search_page import SearchPage


class TestProductDetails(BaseTest):
    def test_verify_product_details(self):
        self.driver.get(locators.base_url)
        search = SearchPage(self.driver)
        search.search("Laptop")
        search.select_product_by_index(1)

        # Verify details
        product_page = ProductPage(self.driver)
        self.assertTrue(
            product_page.verify_product_details(
                expected_name="Lenovo Thinkpad Carbon Laptop",
                expected_price="नेरू 1,360.00"
            ),
            "Product details verification failed"
        )


if __name__ == "__main__":
    unittest.main()