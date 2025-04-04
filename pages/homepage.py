from base.basedriver import Basedriver
from utilities.locators import Homepage_locators
from pages.signup_login_page import Signup_Login_page
from pages.contact_us_page import ContactUs_page
from pages.testcases_page import Testcases_Page


class Homepage(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Homepage_locators
        
    def homepage_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.home_slider)
            return self.driver.title == 'Automation Exercise'
        except Exception:
            return False 
        
    def click_signup_login_btn(self):
        self.go_to_signup_login_page()
        return Signup_Login_page(self.driver)
    
    def click_contact_us_btn(self):
        self.go_to_contact_us_page()
        return ContactUs_page(self.driver)   

    def click_testcases_btn(self):
        self.go_to_testcases_page()
        return Testcases_Page(self.driver)
    
    