import unittest
import locators
from basePage.base_test import BaseTest
from pages.search_page import SearchPage


class TestSearch(BaseTest):

    def test_search_valid_product(self):
        self.driver.get(locators.base_url)
        search = SearchPage(self.driver)
        product = "Iphone"
        search.search(product)

        self.assertTrue(
            search.are_results_displayed(),
            f"No results displayed for valid product: {product}"
        )
        search.open_product_page()
        print("TC-03")

    def test_search_invalid_product(self):
        self.driver.get(locators.base_url)
        search = SearchPage(self.driver)
        product = "!@#$%"
        search.search(product)

        self.assertTrue(
            search.get_no_results_message(),
            f"Results displayed for: {product}"
        )

        print("TC-04")

if __name__ == "__main__":
    unittest.main()