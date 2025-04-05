from base.basedriver import Basedriver
from utilities.locators import Cart_page_locators


class Cart_page(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Cart_page_locators
        
    # def subscription_isvisible(self):
    #     try:
    #         self.wait_until_element_is_visible(self.locators.subscription_text)
    #         return True
    #     except Exception:
    #         return False
        
    # def enter_subscription_email(self, emailID):
    #     self.send_keys(self.locators.subscribe_email_field, emailID)    
        
        
        
        
        
        
        
        