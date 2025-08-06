import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import locators
from pages.login_page import LoginPage


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")
        service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get(locators.login_url)
        login = LoginPage(self.driver)
        login.login("manashmaharjan@gmail.com","manash123",True)
        login.verify()
        print("TC-11")

    def test_invalid_login(self):
        self.driver.get(locators.login_url)
        login = LoginPage(self.driver)
        login.login("admin@gmail.com","helloo")
        login.verify_invalid_login()
        print("TC-12")

    def test_sql_injection(self):
        self.driver.get(locators.login_url)
        login = LoginPage(self.driver)
        login.login("' OR '1'='1","anything")
        login.verify_sql_injection()
        print("TC-13")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()