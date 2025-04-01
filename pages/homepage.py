from base.basedriver import Basedriver
from utilities.locators import Homepage_locators


class Homepage(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Homepage_locators
        
    def click_signup_login_btn(self):
        self.click_on_element(self.locators.signup_login_btn)
        
    def click_contact_us_btn(self):
        self.click_on_element(self.locators.contact_us_btn)
        
    def click_test_cases_btn(self):
        self.click_on_element(self.locators.test_cases_btn)
        
    def click_products_btn(self):
        self.click_on_element(self.locators.products_btn)
        
    def click_cart_btn(self):
        self.click_on_element(self.locators.cart_btn)
        
    def click_view_product(self):
        self.click_on_element(self.locators.view_product)
        
    def click_add_to_cart(self):
        self.click_on_element(self.locators.add_to_cart)
        
    