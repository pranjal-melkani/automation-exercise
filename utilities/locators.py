from selenium.webdriver.common.by import By


class Homepage_locators:
    signup_login_btn = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    contact_us_btn = (By.XPATH, "//a[contains(text(), 'Contact us')]")
    test_cases_btn = (By.XPATH, "//a[contains(text(), 'Test Cases')]")
    products_btn = (By.XPATH, "//a[contains(text(), 'Products')]")
    cart_btn = (By.XPATH, "//a[contains(text(), 'Cart')]")
    view_product = (By.LINK_TEXT, "View Product")
    add_to_cart = (By.LINK_TEXT, "Add to cart")
    
class Signup_Login_page_locators:
    signup_form = (By.CLASS_NAME, "signup-form")
    signup_header = (By.XPATH, "//*[text()='New User Signup!']")
    signup_name_field = (By.XPATH, "//*[@data-qa='signup-name']")
    signup_email_field = (By.XPATH, "//*[@data-qa='signup-email']")
    signup_btn = (By.XPATH, "//*[@data-qa='signup-button']")
    
    # Signup page
    enter_account_info_header = (By.XPATH, "//*[text()='Enter Account Information']")
    title_mr = (By.ID, "id_gender1")
    title_mrs = (By.ID, "id_gender2")
    password_field = (By.ID, "password")
    dob_day_field = (By.ID, "days")
    dob_month_field = (By.ID, "months")
    dob_year_field = (By.ID, "years")
    
    
    