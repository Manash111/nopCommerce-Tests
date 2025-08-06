from base_page import BasePage
import locators
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(BasePage):
    def login(self, email, password, remember_me=False):
        self.type_text(locators.input_email_login, email)
        self.type_text(locators.input_password_login, password)
        if remember_me:
            self.click(locators.checkbox_rememberMe)
        else:
            print("Checkbox not checked")
        self.click(locators.btn_login)

    def logout(self):
        self.click(locators.btn_logout)
    def verify(self):
        expected_title = "Your store. Home page title"
        title = self.get_title()
        if title == expected_title:
            print("Test Passed")

    def verify_invalid_login(self):
        self.wait.until(EC.url_contains("login"))
        assert "Login was unsuccessful" in self.driver.page_source
        print("verification completed")

    def verify_sql_injection(self):
        self.wait.until(EC.url_contains("login"))
        assert "Please enter a valid email address" in self.driver.page_source
        print("sql injection verification completed")