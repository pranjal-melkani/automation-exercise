from base.basedriver import Basedriver
from utilities.locators import Contactus_page_locators


class ContactUs_page(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Contactus_page_locators
        
    def get_in_touch_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.get_in_touch_text)
            return True
        except Exception:
            return False
    
    def enter_name(self, name):
        self.send_keys(self.locators.name_field, name)
        
    def enter_email(self, email_id):
        self.send_keys(self.locators.email_field, email_id)
        
    def enter_subject(self, subject):
        self.send_keys(self.locators.subject_field, subject)
        
    def enter_message(self, message):
        self.click_on_element(self.locators.message_field)
        self.send_keys(self.locators.message_field, message)
        
    def upload_file(self, filepath):
        self.send_keys(self.locators.file_upload_field, filepath)
    
    def click_on_submit_button(self):
        self.click_on_element(self.locators.submit_btn)
        current_window = self.driver.current_window_handle
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.window(current_window)

    def enter_details(self, name, email_id, subject, message, filepath=""):
        self.enter_name(name)
        self.enter_email(email_id)
        self.enter_subject(subject)
        self.enter_message(message)
        self.upload_file(filepath)
        self.click_on_submit_button()
        
    def success_msg_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.success_message)
            return True
        except Exception:
            return False
        
    def click_on_home_btn(self):
        self.click_on_element(self.locators.home_btn)
        
    