from pages.homepage import Homepage
from utilities.testdata import Testdata
import pytest


class TestHome:
    @pytest.mark.skip
    def test_verify_subscription(self, driver):
        emailID = "testemailID@gmail.com"
        
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        hp.scroll_to_the_bottom()
        assert hp.subscription_isvisible(), \
            "'SUBSCRIPTION' is not visible"
        hp.enter_subscription_email(emailID)
        hp.click_subscribe_arrow()
        assert hp.subscription_success_msg_isvisible(), \
            "'You have been successfully subscribed!' is not visible"