from base.basedriver import Basedriver
from utilities.locators import Cart_page_locators


class Cart_page(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Cart_page_locators
    
    def get_cart_size(self):
        all_items_list = self.get_all_items(self.locators.cart_items_row)
        return len(all_items_list)
    
    def get_cart_item_description(self, product_index):
        all_item_description_list = self.get_all_items(self.locators.cart_item_description)
        target_element = all_item_description_list[product_index]
        return target_element.text
    
    def get_cart_item_price(self, product_index):
        all_item_price_list = self.get_all_items(self.locators.cart_item_price)
        target_element = all_item_price_list[product_index]
        return int(str(target_element.text).replace('Rs. ', ''))
    
    def get_cart_item_quantity(self, product_index):
        all_item_quantity_list = self.get_all_items(self.locators.cart_item_quantity)
        target_element = all_item_quantity_list[product_index]
        return int(target_element.text)
        
    def get_cart_item_total_price(self, product_index):
        all_item_totalprice_list = self.get_all_items(self.locators.cart_item_total)
        target_element = all_item_totalprice_list[product_index]
        return int(str(target_element.text).replace('Rs. ', ''))
     
    def get_cart_items(self):
        cart_items = []
        for i in range(self.get_cart_size()):
            cart_items.append({
                self.get_cart_item_description(i) : {
                    'price' : self.get_cart_item_price(i),
                    'quantity' : self.get_cart_item_quantity(i),
                    'total_price' : self.get_cart_item_total_price(i)
                }
            })
        return cart_items
    
       
        
        
        
        
        
        
        