from selenium.webdriver.common.by import By

#urls
base_url = "http://localhost:5000/"
register_url = f"{base_url}register?returnUrl=%2F"
login_url = f"{base_url}login?returnUrl=%2F"

#links
link_register = (By.XPATH,"//a[normalize-space()='Register']")
link_login = (By.XPATH,"//a[normalize-space()='Log in']")
link_wishList = (By.XPATH,"//a[@class='ico-wishlist']")
link_shoppingCart = (By.XPATH,"//a[@class='ico-cart']")

btn_logout = (By.XPATH,"//a[normalize-space()='Log out']")


#register
radio_male = (By.XPATH,"//input[@id='gender-male']")
radio_female = (By.XPATH,"//input[@id='gender-female']")
input_firstName = (By.XPATH,"//input[@id='FirstName']")
input_lastName = (By.XPATH,"//input[@id='LastName']")
input_email = (By.XPATH,"//input[@id='Email']")
input_companyName = (By.XPATH,"//input[@id='Company']")
checkbox_newsLetter = (By.XPATH,"//input[@id='Newsletter']")
input_password = (By.XPATH,"//input[@id='Password']")
input_confirmPassword = (By.XPATH,"//input[@id='ConfirmPassword']")
btn_register = (By.XPATH,"//button[@id='register-button']")

#login
input_email_login = (By.XPATH,"//input[@id='Email']")
input_password_login = (By.XPATH,"//input[@id='Password']")
checkbox_rememberMe = (By.XPATH,"//input[@id='RememberMe']")
btn_login = (By.XPATH,"//button[normalize-space()='Log in']")