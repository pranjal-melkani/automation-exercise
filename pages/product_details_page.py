from base.basedriver import Basedriver
from utilities.locators import Product_Details_page_locators


class ProductDetails_page(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Product_Details_page_locators
        
    def product_details_page_isvisible(self):
        return self.driver.title.__contains__('Product Details')
    
    def product_category_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.product_category)
            return True
        except Exception:
            raise AssertionError("Product Category is not visible")
        
    def product_availability_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.product_availability)
            return True
        except Exception:
            raise AssertionError("Product Availability is not visible")
    
    def product_condition_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.product_condition)
            return True
        except Exception:
            raise AssertionError("Product Condition is not visible")
    
    def product_brand_isvisible(self):
        try:
            self.wait_until_element_is_visible(self.locators.product_brand)
            return True
        except Exception:
            raise AssertionError("Product Brand is not visible")
    
    def all_product_details_arevisible(self):
        try:
            self.product_category_isvisible()
            self.product_availability_isvisible()
            self.product_condition_isvisible()
            self.product_brand_isvisible()
            return True
        except Exception:
            return False
    
    
    