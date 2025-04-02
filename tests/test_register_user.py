from utilities.testdata import Testdata
from pages.homepage import Homepage
from faker import Faker

import pytest

@pytest.mark.skip
class TestRegisterUser:
    def test_new_registration(self, driver):
        fake = Faker()
        name = fake.name()
        email_id = fake.email()
        title = "Mr"
        password = "Pass@123"
        dob = str(fake.date_of_birth())
        fname = fake.first_name()
        lname = fake.last_name()
        company = fake.company()
        address1 = fake.address()
        address2 = fake.address()
        country = "United States"
        state = fake.state()
        city = fake.city()
        zip_code = fake.zipcode()
        mob_no = fake.phone_number()
        
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        slp = hp.click_signup_login_btn()
        assert slp.signup_field_isvisible(), \
            "Signup field is not visible"
        slp.signup_user(name, email_id)
        assert slp.enter_account_info_isvisible(), \
            "'Enter Account Information' is not visible"
        slp.fill_additional_signup_details(title, password, dob, fname, lname, company, address1, 
                                       address2, country, state, city, zip_code, mob_no)  
        assert slp.account_created_isvisible(), \
            "'ACCOUNT CREATED!' is not visible"
        slp.click_continue_btn()
        logged_in_text = slp.get_logged_in_user_details()
        assert logged_in_text.__contains__(f"Logged in as {name}"), \
            f"'Logged in as {name}' is not visible"
        slp.click_delete_account_btn()
        assert slp.account_deleted_isvisible(), \
            "'ACCOUNT DELETED!' is not visible"
        slp.click_continue_btn()
    
    
    def test_duplicate_registration(self, driver):
        name = "TEST ADMIN"
        email_id = "testingemail_admin@gmail.com"
        
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        slp = hp.click_signup_login_btn()
        assert slp.signup_field_isvisible(), \
            "Signup field is not visible"
        slp.signup_user(name, email_id)
        assert slp.email_exists_error_isvisible(), \
            "'Email Address already exist!' is not visible"
        