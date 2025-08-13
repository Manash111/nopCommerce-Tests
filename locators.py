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


#navigation TOP MENU ITEMS
link_computer = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']")
link_electronics = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']")
link_apparel = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Apparel']")
link_digitalDownloads = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Digital downloads']")
link_books = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Books']")
link_jewelry = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Jewelry']")
link_giftcards = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Gift Cards']")

#search

input_search = (By.XPATH,"//input[@id='small-searchterms']")
btn_search = (By.XPATH,"//button[normalize-space()='Search']")
list_product = (By.CSS_SELECTOR,".product-item")
noresult_msg = (By.CSS_SELECTOR,".no-result")


#productDetails
product_name = (By.CSS_SELECTOR,".product-name")
product_description = (By.CSS_SELECTOR,".short-description")
product_price = (By.CSS_SELECTOR,".product-price span")
product_image = (By.XPATH,"//div[@class ='picture-gallery']//div[@class = 'picture']")

#product link
click_product = (By.XPATH, "//h2[@class = 'product-title']/a")


btn_addToCart = (By.XPATH,"//button[@class='button-2 product-box-add-to-cart-button']")
btn_addToCart_product_page = (By.XPATH,"//button[@class='button-1 add-to-cart-button']")
cart_quantity = (By.XPATH,"//span[@class='cart-qty']")

btn_goto_cart = (By.XPATH, "//span[@class='cart-label']")
btn_remove_product = (By.XPATH, "//tbody//td[7]/button")
# empty_cart_message = (By.XPATH,"//div[@class='no-data']")

btn_shopping_cart_popup = (By.XPATH, "//*[@id='bar-notification']/div/p/a")


#Checkout

checkbox_termsOfService = (By.XPATH,"//input[@id='termsofservice']")
btn_checkout = (By.XPATH,"//button[@id='checkout']")

#checkout as guest
btn_checkout_guest = (By.XPATH,"//button[normalize-space()='Checkout as Guest']")

#billing address

input_firstName_guestCheckout = (By.XPATH,"//input[@id='BillingNewAddress_FirstName']")
input_lastName_guestCheckout = (By.XPATH,"//input[@id='BillingNewAddress_LastName']")
input_email_guestCheckout = (By.XPATH,"//input[@id='BillingNewAddress_Email']")
input_companyName_guestCheckout = (By.XPATH,"//input[@id='BillingNewAddress_Company']")
select_country_guestCheckout = (By.XPATH,"//select[@id='BillingNewAddress_CountryId']")
select_state_guestCheckout = (By.XPATH,"//select[@id='BillingNewAddress_StateProvinceId']")
input_city_guestCheckout = (By.XPATH,"//input[@id='BillingNewAddress_City']")
input_address1_guestCheckout = (By.XPATH,"//input[@id='BillingNewAddress_Address1']")
input_address2_guestCheckout = (By.XPATH,"//input[@id='BillingNewAddress_Address2']")
input_zipCode_guestCheckout = (By.XPATH,"//input[@id='BillingNewAddress_ZipPostalCode']")
input_phoneNumber_guestCheckout = (By.XPATH,"//input[@id='BillingNewAddress_PhoneNumber']")
input_faxNumber_guestCheckout = (By.XPATH,"//input[@id='BillingNewAddress_FaxNumber']")
btn_continue_to_shipping_method = (By.XPATH, "//*[@id='billing-buttons-container']/button[2]")
#shipping method
radio_ground = (By.XPATH, "//input[@id='shippingoption_0']")
radio_air =(By.XPATH, "input[@id='shippingoption_0']")
radio_twoDayAir = (By.XPATH,"input[@id='shippingoption_2']")
btn_continue_to_payment = (By.XPATH,"//button[@class='button-1 shipping-method-next-step-button']")

#payemnt method
radio_check = (By.XPATH, "//input[@id='paymentmethod_0']")
radio_creditCard = (By.XPATH, "//input[@id='paymentmethod_1']")
btn_continue_to_payment_info = (By.XPATH, "//button[@class='button-1 payment-method-next-step-button']")

#credit card

select_card_type = (By.XPATH, "//select[@id='CreditCardType']")
input_cardHolder_name = (By.XPATH, "//input[@id='CardholderName']")
input_cardNumber = (By.XPATH, "//input[@id='CardNumber']")
select_exp_month = (By.XPATH, "//select[@id='ExpireMonth']")
select_exp_year = (By.XPATH, "//select[@id='ExpireYear']")
input_cardCode = (By.XPATH, "//input[@id='CardCode']")

btn_confirm = (By.XPATH, "//button[normalize-space()='Confirm']")

btn_continue_to_confirm = (By.XPATH,"//*[@id='payment-info-buttons-container']/button")

order_confirmation = (By.XPATH,"//strong[normalize-space()='Your order has been successfully processed!']")

