from pages.homepage import Homepage
from utilities.testdata import Testdata
import pytest


class TestCart:
    @pytest.mark.skip
    def test_verify_subscription(self, driver):
        emailID = "testemailID@gmail.com"
        
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        cp = hp.click_cart_btn()
        cp.scroll_to_the_bottom()
        assert cp.subscription_isvisible(), \
            "'SUBSCRIPTION' is not visible"
        cp.enter_subscription_email(emailID)
        cp.click_subscribe_arrow()
        assert cp.subscription_success_msg_isvisible(), \
            "'You have been successfully subscribed!' is not visible"