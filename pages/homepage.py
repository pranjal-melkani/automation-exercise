from base.basedriver import Basedriver
from utilities.locators import Homepage_locators
from pages.signup_login_page import Signup_Login_page


class Homepage(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Homepage_locators
        
    def homepage_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.navbar_home)
            self.wait_until_element_is_visible(self.navbar_products)
            return self.driver.title == 'Automation Exercise'
        except Exception:
            return False 
        
    def click_signup_login_btn(self):
        self.go_to_signup_login_page()
        return Signup_Login_page(self.driver)
        
        
        
        
        
        
        
    
        
    def click_contact_us_btn(self):
        self.click_on_element(self.locators.contact_us_btn)
        
    def click_test_cases_btn(self):
        self.click_on_element(self.locators.test_cases_btn)
        
    def click_products_btn(self):
        self.click_on_element(self.locators.products_btn)
        
    def click_cart_btn(self):
        self.click_on_element(self.locators.cart_btn)
        
    def click_view_product_btn(self):
        self.click_on_element(self.locators.view_product)
        
    def click_add_to_cart_btn(self):
        self.click_on_element(self.locators.add_to_cart)
    
    def click_home_btn(self):
        self.click_on_element(self.locators.home_btn)
    
    def click_logout_btn(self):
        self.click_on_element(self.locators.logout_btn)
        
    