from base.basedriver import Basedriver
from utilities.locators import AllProducts_page_locators
from pages.product_details_page import ProductDetails_page
from pages.cart_page import Cart_page


class AllProductsPage(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AllProducts_page_locators
        self.products_in_cart = []
        
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
    
    def hover_mouse_over_a_product(self, product_index):
        all_product_list = self.get_all_items(self.locators.single_product)
        target_element = all_product_list[product_index]
        self.hover_mouse_over_element(target_element)
    
    def click_add_to_cart(self, product_index):
        all_add_to_cart_btn_list = self.get_all_items(self.locators.add_to_cart_overlay_btn)
        target_element = all_add_to_cart_btn_list[product_index]
        self.hover_mouse_and_click_element(target_element)
    
    def get_product_description(self, product_index):
        all_products_description_list = self.get_all_items(self.locators.product_description)
        target_element = all_products_description_list[product_index]
        return target_element.text
    
    def get_product_price(self, product_index):
        all_products_price_list = self.get_all_items(self.locators.product_price)
        target_element = all_products_price_list[product_index]
        return int(str(target_element.text).replace('Rs. ', ''))
    
    def update_cart(self, product, price):
        product_list = [list(product.keys())[0] for product in self.products_in_cart]
        if product not in product_list:
            self.products_in_cart.append({
                product : {
                    'price' : price,
                    'quantity' : 1
                }
            })
        else:
            index = product_list.index(product)
            self.products_in_cart[index][product]['quantity'] += 1 
            
    def get_products_added_in_cart(self):
        return self.products_in_cart
       
    def add_product_to_cart(self, product_index):
        self.hover_mouse_over_a_product(product_index)
        product_description = self.get_product_description(product_index)
        product_price = self.get_product_price(product_index)
        self.update_cart(product_description, product_price)
        self.click_add_to_cart(product_index)
    
    def click_continue_shopping_btn(self):
        self.click_on_element(self.locators.continue_shopping_btn)
        
    def click_view_cart_btn(self):
        self.click_on_element(self.locators.view_cart_btn)
        return Cart_page(self.driver)
    

    
    
    
        