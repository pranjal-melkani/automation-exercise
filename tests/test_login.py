from utilities.testdata import Testdata
from pages.homepage import Homepage
import pytest

@pytest.mark.skip
class TestLogin:
    def test_invalid_login(self, driver):
        email_id = "admin@gmail.com"
        password = "admin"
            
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        slp = hp.click_signup_login_btn()
        assert slp.login_field_isvisible(), \
            "Login field is not visible"
        slp.login_user(email_id, password)
        assert slp.incorrect_credentials_error_isvisible(), \
            "'Your email or password is incorrect!' is not visible"   
    
    
    def test_valid_login(self, driver):
        name = "TEST ADMIN"
        email_id = "testingemail_admin@gmail.com"
        password = "admin"
        
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        slp = hp.click_signup_login_btn()
        assert slp.login_field_isvisible(), \
            "Login field is not visible"
        slp.login_user(email_id, password)
        logged_in_text = slp.get_logged_in_user_details()
        assert logged_in_text.__contains__(f"Logged in as {name}"), \
            f"'Logged in as {name}' is not visible"
        
        
    def test_logout(self, driver):
        email_id = "testingemail_admin@gmail.com"
        password = "admin"
        
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        slp = hp.click_signup_login_btn()
        assert slp.login_field_isvisible(), \
            "Login field is not visible"
        slp.login_user(email_id, password)
        slp.logout()
        assert str(driver.current_url).__contains__('login'), \
            "User is not navigated back to login page"

        
        
    
            
            