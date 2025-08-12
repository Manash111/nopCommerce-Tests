from basePage.base_page import BasePage
import locators


class HomePage(BasePage):

    def verify(self):
        expected_title = "Your store. Home page title"
        title = self.get_title()
        if title == expected_title:
            print("Verified")

    def navigation_top_menu(self):
        self.click(locators.link_computer)
        self.click(locators.link_electronics)
        self.click(locators.link_apparel)
        self.click(locators.link_digitalDownloads)
        self.click(locators.link_books)
        self.click(locators.link_giftcards)
        print("Navigation successful")
