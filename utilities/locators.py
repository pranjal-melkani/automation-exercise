from selenium.webdriver.common.by import By


class Homepage_locators:
    signup_login_btn = (By.PARTIAL_LINK_TEXT, "Signup / Login")
    contact_us_btn = (By.PARTIAL_LINK_TEXT, "Contact us")
    test_cases_btn = (By.PARTIAL_LINK_TEXT, "Test Cases")
    products_btn = (By.PARTIAL_LINK_TEXT, "Products")
    cart_btn = (By.PARTIAL_LINK_TEXT, "Cart")
    view_product = (By.LINK_TEXT, "View Product")
    add_to_cart = (By.LINK_TEXT, "Add to cart")
    