from pages.homepage import Homepage
from utilities.testdata import Testdata


class TestTestcasesPage:
    def test_verify_testcases_page(self, driver):
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        tp = hp.click_testcases_btn()
        assert tp.testcases_pages_isvisible(),\
            "Test Cases page is not visible. Some elements are missing, or webpage title does not contain 'Test Cases'"
        