import unittest

import locators
from pages.homepage_page import HomePage
from basePage.base_test import BaseTest


class TestHomePage(BaseTest):
    def test_homepage(self):
        self.driver.get(locators.base_url)
        homepage = HomePage(self.driver)
        homepage.verify()
        print("TC01")

        #test navigation
        homepage.navigation_top_menu()
        print("TC02")


if __name__ == "__main__":
    unittest.main()
