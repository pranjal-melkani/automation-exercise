from datetime import datetime
import time
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
        month_dict = {'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June',
                      '7':'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':'December'}
        self.select_dropdown_by_visible_text(self.locators.dob_day_field, str(day))
        self.select_dropdown_by_visible_text(self.locators.dob_month_field, month_dict[str(month)])
        self.select_dropdown_by_visible_text(self.locators.dob_year_field, str(year))
    
    def subscribe_newsletter(self):
        if not self.wait_until_element_is_visible(self.locators.newsletter_checkbox).is_selected():
            self.click_on_element(self.locators.newsletter_checkbox)
            
    def subscribe_special_offer(self):
        if not self.wait_until_element_is_visible(self.locators.special_offer_checkbox).is_selected():
            self.click_on_element(self.locators.special_offer_checkbox)
            
    def enter_first_name(self, fname):
        self.send_keys(self.locators.first_name_field, fname)
        
    def enter_last_name(self, lname):
        self.send_keys(self.locators.last_name_field, lname)
        
    def enter_company(self, company):
        self.send_keys(self.locators.company_field, company)
        
    def enter_address1(self, address):
        self.send_keys(self.locators.address1_field, address)
        
    def enter_address2(self, address):
        self.send_keys(self.locators.address2_field, address)
        
    def select_country(self, country):
        self.select_dropdown_by_visible_text(self.locators.country_dropdown, country)
        
    def enter_state(self, state):
        self.send_keys(self.locators.state_field, state)
    
    def enter_city(self, city):
        self.send_keys(self.locators.city_field, city)
        
    def enter_zip_code(self, zip_code):
        self.send_keys(self.locators.zipcode_field, zip_code) 
    
    def enter_mobile_number(self, mob_no):
        self.send_keys(self.locators.mobile_no_field, mob_no)  
    
    def click_create_account_btn(self):
        self.click_on_element(self.locators.create_account_btn)
        
    def fill_additional_signup_details(self, title, password, dob, fname, lname, company, address1, 
                                       address2, country, state, city, zip_code, mob_no):
        self.enter_title(title)
        self.enter_password(password)
        self.enter_date_of_birth(dob)
        self.subscribe_newsletter()
        self.subscribe_special_offer()
        self.enter_first_name(fname)
        self.enter_last_name(lname)
        self.enter_company(company)
        self.enter_address1(address1)
        self.enter_address2(address2)
        self.select_country(country)
        self.enter_state(state)
        self.enter_city(city)
        self.enter_zip_code(zip_code)
        self.enter_mobile_number(mob_no)
        time.sleep(10)
        self.click_create_account_btn()
        
    def account_created_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.account_created_message)
            return True
        except Exception:
            return False
        
    def click_continue_btn(self):
        self.click_on_element(self.locators.continue_btn)
        
    def get_logged_in_as_value(self):
        return self.wait_until_element_is_visible(self.locators.logged_in_as_field).text
    
    def click_delete_account_btn(self):
        self.click_on_element(self.locators.delete_account_btn)
        
    def account_deleted_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.account_deleted_message)
            return True
        except Exception:
            return False