from datetime import datetime
from base.basedriver import Basedriver
from utilities.locators import Signup_Login_page_locators


class Signup_Login_page(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Signup_Login_page_locators
        
    def signup_field_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.signup_form)
            self.wait_until_element_is_visible(self.locators.signup_header)
            return True
        except Exception:
            return False
        
    def enter_signup_name(self, name):
        self.send_keys(self.locators.signup_name_field, name)
        
    def enter_signup_email(self, email_id):
        self.send_keys(self.locators.signup_email_field, email_id)
        
    def click_signup_btn(self):
        self.click_on_element(self.locators.signup_btn)
        
    def signup_user(self, name, email_id):
        self.enter_signup_name(name)
        self.enter_signup_email(email_id)
        self.click_signup_btn()
        
    def enter_account_info_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.enter_account_info_header)
            return True
        except Exception:
            return False
        
    def enter_title(self, title):
        if str(title).lower() == 'mr':
            self.click_on_element(self.locators.title_mr)
        else:
            self.click_on_element(self.locators.title_mrs)
    
    def enter_password(self, password):
        self.send_keys(self.locators.password_field, password)
        
    def enter_date_of_birth(self, dob):
        date_object = datetime.strptime(dob, "%Y-%m-%d")
        day = date_object.day
        month = date_object.month
        year = date_object.year
        month_dict = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June',
                      '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
        self.select_dropdown_by_visible_text(self.locators.dob_day_field, str(day))
        self.select_dropdown_by_visible_text(self.locators.dob_month_field, month_dict[str(month)])
        self.select_dropdown_by_visible_text(self.locators.dob_year_field, str(year))