from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from utilities.testdata import Testdata
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Basedriver:
    navbar_home = (By.XPATH, "//a[contains(text(), 'Home')]")
    navbar_products = (By.XPATH, "//a[contains(text(), 'Products')]")
    navbar_cart = (By.XPATH, "//a[contains(text(), 'Cart')]")
    navbar_signup_login = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    navbar_testcases = (By.XPATH, "//a[contains(text(), 'Test Cases')]")
    navbar_api_testing = (By.XPATH, "//a[contains(text(), 'API Testing')]")
    navbar_contact_us = (By.XPATH, "//a[contains(text(), 'Contact us')]")
    navbar_loggedinas_field = (By.CSS_SELECTOR, ".navbar-nav li:last-child")
    navbar_logout = (By.XPATH, "//a[contains(text(), 'Logout')]")
    
    footer_subscription_text = (By.XPATH, "//*[text()='Subscription']")
    footer_subscribe_email_field = (By.ID, "susbscribe_email")
    footer_subscribe_arrow = (By.ID, "subscribe")
    footer_subscription_success_msg = (By.XPATH, "//*[text()='You have been successfully subscribed!']")
    
    def __init__(self, driver):
        self.driver = driver
        
    def wait_until_element_is_visible(self, locator):
        wait = WebDriverWait(self.driver, timeout=Testdata.timeout)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element
    
    def click_on_element(self, locator):
        element = self.wait_until_element_is_visible(locator)
        element.click()
        
    def send_keys(self, locator, input_text):
        element = self.wait_until_element_is_visible(locator)
        element.clear()
        element.send_keys(input_text)
        
    def select_dropdown_by_visible_text(self, locator, visible_text):
        element = self.wait_until_element_is_visible(locator)
        Select(element).select_by_visible_text(visible_text)
        
    def get_all_items(self, locator):
        return self.driver.find_elements(locator[0], locator[1])
        
    def open_url(self, url):
        self.driver.get(url)
        
    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def scroll_to_specific_element(self, locator):
        element = self.wait_until_element_is_visible(locator)
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).perform()
        
    def hover_mouse_over_element(self, element):
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).move_to_element(element).perform()
        
    def hover_mouse_and_click_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()
    
    # Navbar    
    def go_to_homepage(self):
        self.click_on_element(self.navbar_home)

    def open_cart(self):
        self.click_on_element(self.navbar_cart)
        
    def go_to_signup_login_page(self):
        self.click_on_element(self.navbar_signup_login)
        
    def get_logged_in_user_details(self):
        return self.wait_until_element_is_visible(self.navbar_loggedinas_field).text
    
    def logout(self):
        self.click_on_element(self.navbar_logout)
        
    def go_to_contact_us_page(self):
        self.click_on_element(self.navbar_contact_us)
        
    def go_to_testcases_page(self):
        self.click_on_element(self.navbar_testcases)
        
    def go_to_products_page(self):
        self.click_on_element(self.navbar_products)
    
    # Footer    
    def subscription_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.footer_subscription_text)
            return True
        except Exception:
            return False
        
    def enter_subscription_email(self, emailID):
        self.send_keys(self.footer_subscribe_email_field, emailID)
        
    def click_subscribe_arrow(self):
        self.click_on_element(self.footer_subscribe_arrow)
        
    def subscription_success_msg_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.footer_subscription_success_msg)
            return True
        except Exception:
            return False