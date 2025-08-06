from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import locators
from pages.register_page import RegisterPage
import unittest


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")
        service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service,options=options)
        cls.driver.maximize_window()

    def test_register(self):
        self.driver.get(locators.register_url)
        register = RegisterPage(self.driver)
        register.personal_details("male","Manash","Maharjan","manashmaharjan@gmail.com")
        register.set_credentials("manash@123","manash@123","")
        register.click_register()
        register.verify()
        print("TC-10")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()