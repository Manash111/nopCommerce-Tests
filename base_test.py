from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")
        service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()