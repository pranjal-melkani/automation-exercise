import os
from utilities.testdata import Testdata
from pages.homepage import Homepage
from faker import Faker


class TestContactUs:
    def test_contact_us(self, driver):
        fake = Faker()
        name = fake.name()
        email = fake.email()
        subject = "Test Subject"
        message = fake.text()
        filepath = os.path.join(os.getcwd(), "testdata", "uploadfile.txt")
        
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        cp = hp.click_contact_us_btn()
        assert cp.get_in_touch_isvisible(), \
            "'GET IN TOUCH' is not visible"
        cp.enter_details(name, email, subject, message, filepath)
        assert cp.success_msg_isvisible(), \
            "'Success! Your details have been submitted successfully.' message is not visible"
        cp.click_on_home_btn()
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"