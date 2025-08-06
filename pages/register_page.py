from base_page import BasePage
import locators
from selenium.webdriver.support import expected_conditions as EC



class RegisterPage(BasePage):
    def personal_details(self,gender, firstname, lastname, email):
        gender = gender.lower()
        if gender == "male":
            self.click(locators.radio_male)
        else:
            self.click(locators.radio_female)

        self.type_text(locators.input_firstName,firstname)
        self.type_text(locators.input_lastName,lastname)
        self.type_text(locators.input_email,email)

    def set_credentials(self , password, confirm_password, company_name, newsletter=False):
        self.type_text(locators.input_companyName,company_name)
        if newsletter:
            self.click(locators.checkbox_newsLetter)
        else:
            print("newsletter not checked")
        self.type_text(locators.input_password,password)
        self.type_text(locators.input_confirmPassword,confirm_password)

    def click_register(self):
        self.click(locators.btn_register)

    def verify(self):
        self.wait.until(EC.url_contains("registerresult"))
        assert "Your registration completed" in self.driver.page_source
        print("registration test passed")

