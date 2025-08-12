import unittest

import locators
from basePage.base_test import BaseTest
from pages.cart_page import CartPage
from pages.search_page import SearchPage
from pages.checkout_page import CheckoutPage


class TestGuestCheckout(BaseTest):
    def test_guest_checkout_flow(self):
        self.driver.get(locators.base_url)
        # Test Data
        product = "iPhone"
        guest_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': f"john.doe@test.com",
            'country': 'Nepal',
            'state': 'Bagmati',
            'city': 'Kathmandu',
            'address1': '22',
            'zip_code': '5050',
            'phone': '9841828282'
        }
        payment_method = "check"  # or "credit"

        # Initialize Pages
        search_page = SearchPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        # Test Steps
        search_page.search(product)
        cart_page.add_to_cart(0)  # Add first search result
        cart_page.goto_cart()
        checkout_page.start_guest_checkout()
        checkout_page.fill_billing_address(guest_data)
        checkout_page.select_shipping_method()
        checkout_page.select_payment_method(payment_method)

        if payment_method == "credit":
            checkout_page.fill_credit_card_details({
                'type': 'Visa',
                'name': 'John Doe',
                'number': '4111111111111111',
                'exp_month': '05',
                'exp_year': '2025',
                'code': '123'
            })

        confirmation_text = checkout_page.confirm_order()

        # Verification
        self.assertIn("Your order has been successfully processed!", confirmation_text)
        print(f"Order confirmed. Number: {confirmation_text.split('#')[-1]}")


if __name__ == "__main__":
    unittest.main()