from base.basedriver import Basedriver
from utilities.locators import AllProducts_page_locators
from pages.product_details_page import ProductDetails_page


class AllProductsPage(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AllProducts_page_locators
        
    def all_products_page_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.all_products_text)
            return self.driver.title.__contains__('All Products')
        except Exception:
            return False
        
    def product_list_isvisible(self):
        try:
            all_product_list = self.get_all_items(self.locators.single_product)
            return len(all_product_list) >= 1
        except Exception:
            return False
        
    def click_on_first_view_product(self):
        self.click_on_element(self.locators.view_product_link)
        return ProductDetails_page(self.driver)
    
    def enter_productname_in_search_field(self, productName):
        self.send_keys(self.locators.search_product_field, productName)
    
    def click_search_btn(self):
        self.click_on_element(self.locators.search_btn)
        
    def search_product(self, productName):
        self.enter_productname_in_search_field(productName)
        self.click_search_btn()
    
    def searched_products_isvisible(self):
        try:
           self.wait_until_element_is_visible(self.locators.searched_products_text)
           return True 
        except Exception:
            return False
    
    
    
        