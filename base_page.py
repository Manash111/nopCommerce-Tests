from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)  # Default wait

    def click(self, locator):
        """Click any element after waiting for it to be clickable."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        """Clear and type text into an input field."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator, timeout=10):
        """Check if an element is visible (with custom timeout)."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    # Navigation
    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text