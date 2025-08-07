import random
from base_page import BasePage
import locators
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    def search(self, product_name):
        self.type_text(locators.input_search, product_name)
        self.click(locators.btn_search)

    def open_product_page(self):
        self.click(locators.click_product)

    def select_product_by_index(self, index=0):
        """Selects product by its position (0-based index)"""
        products = self.wait.until(
            EC.presence_of_all_elements_located(locators.click_product)
        )
        products[index].click()

    def select_random_product(self):
        """Clicks a random product from search results"""
        products = self.wait.until(
            EC.presence_of_all_elements_located(locators.click_product)
        )
        random.choice(products).click()

    def select_product_by_name(self, product_name):
        """Clicks product with exact matching name"""
        products = self.wait.until(
            EC.presence_of_all_elements_located(locators.click_product)
        )
        for product in products:
            if product.text.lower() == product_name.lower():
                product.click()
                return
        raise ValueError(f"Product '{product_name}' not found")

    def are_results_displayed(self):
        """Returns True if at least 1 product is displayed"""
        try:
            results = self.wait.until(
                EC.visibility_of_any_elements_located(locators.list_product)
            )
            print("Product Found")
            return len(results) > 0

        except:
            return False

    def get_no_results_message(self):
        """Returns text if 'no products' message appears"""
        try:
            print("No product found")
            return self.wait.until(
                EC.visibility_of_element_located(locators.noresult_msg)
            ).text

        except:
            return None