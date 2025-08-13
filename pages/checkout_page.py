from basePage.base_page import BasePage
import locators
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as EC



class CheckoutPage(BasePage):
    def start_guest_checkout(self):
        """Initiates checkout process"""
        self.click(locators.checkbox_termsOfService)
        self.click(locators.btn_checkout)
        self.click(locators.btn_checkout_guest)

    def fill_billing_address(self, data):
        """Fills guest billing address form with robust dropdown handling"""
        try:
            # Fill text fields
            self.type_text(locators.input_firstName_guestCheckout, data['first_name'])
            self.type_text(locators.input_lastName_guestCheckout, data['last_name'])
            self.type_text(locators.input_email_guestCheckout, data['email'])

            # Handle dropdowns with explicit waits
            country_dropdown = Select(self.find(locators.select_country_guestCheckout))
            country_dropdown.select_by_visible_text(data['country'])

            # Wait for state dropdown to populate (AJAX)
            time.sleep(1)  # Brief pause if needed
            state_dropdown = self.find(locators.select_state_guestCheckout)
            Select(state_dropdown).select_by_visible_text(data['state'])

            # Fill remaining fields
            self.type_text(locators.input_city_guestCheckout, data['city'])
            self.type_text(locators.input_address1_guestCheckout, data['address1'])
            self.type_text(locators.input_zipCode_guestCheckout, data['zip_code'])
            self.type_text(locators.input_phoneNumber_guestCheckout, data['phone'])

            self.click(locators.btn_continue_to_shipping_method)
        except Exception as e:
            print(f"Error in fill_billing_address: {str(e)}")
            raise

    def select_shipping_method(self, method="ground"):
        """Selects shipping method (ground/air/2-day)"""
        methods = {
            "ground": locators.radio_ground,
            "air": locators.radio_air,
            "2day": locators.radio_twoDayAir
        }
        self.click(methods[method.lower()])
        self.click(locators.btn_continue_to_payment)

    def select_payment_method(self, method="check"):
        """Selects payment method (check/credit card)"""
        methods = {
            "check": locators.radio_check,
            "credit": locators.radio_creditCard
        }
        self.click(methods[method.lower()])
        self.click(locators.btn_continue_to_payment_info)

    def check_method(self):
        self.click(locators.btn_continue_to_confirm)

    def fill_credit_card_details(self, card_data):
        """Fills credit card details (if payment method is credit card)"""
        Select(self.driver.find_element(locators.select_card_type)).select_by_visible_text(card_data['type'])
        self.type_text(locators.input_cardHolder_name, card_data['name'])
        self.type_text(locators.input_cardNumber, card_data['number'])
        Select(self.driver.find_element(locators.select_exp_month)).select_by_visible_text(card_data['exp_month'])
        Select(self.driver.find_element(locators.select_exp_year)).select_by_visible_text(card_data['exp_year'])
        self.type_text(locators.input_cardCode, card_data['code'])
        self.click(locators.btn_continue_to_confirm)

    def confirm_order(self):
        """Finalizes order and returns confirmation text"""
        self.click(locators.btn_confirm)
        return self.wait.until(
            EC.visibility_of_element_located(locators.order_confirmation)
        ).text