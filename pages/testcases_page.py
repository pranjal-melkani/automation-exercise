from base.basedriver import Basedriver
from utilities.locators import Testcases_page_locators


class Testcases_Page(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Testcases_page_locators
        
    def testcases_pages_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.testcases_text)
            return self.driver.title.__contains__('Test Cases')
        except Exception:
            return False