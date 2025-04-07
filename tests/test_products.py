import time
from pages.homepage import Homepage
from utilities.testdata import Testdata
import pytest


class TestProducts:
    @pytest.mark.skip
    def test_allProducts(self, driver):
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        ap = hp.click_products_btn()
        assert ap.all_products_page_isvisible(), \
            "All Products page is not visible. Some elements are missing, or webpage title does not \
            contain 'All Products'"
        assert ap.product_list_isvisible(), \
            "Product List is not visible or there are no items displaying currently"
        pd = ap.click_on_first_view_product()
        assert pd.product_details_page_isvisible(), \
            "Product Details page is not visible or webpage title does not contain 'Product Details'"
        assert pd.all_product_details_arevisible(), \
            "Some product details are missing"   
    
    @pytest.mark.skip 
    def test_search_product(self, driver):
        productName = "Summer White Top"
        
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        ap = hp.click_products_btn()
        assert ap.all_products_page_isvisible(), \
            "All Products page is not visible. Some elements are missing, or webpage title does not \
            contain 'All Products'"
        ap.search_product(productName)
        assert ap.searched_products_isvisible(), \
            "'SEARCHED PRODUCTS' is not visible"
        assert ap.product_list_isvisible(), \
            "Product List is not visible or there are no items displaying currently"
    
    @pytest.mark.skip       
    def test_add_products_in_cart(self, driver):
        hp = Homepage(driver)
        hp.open_url(Testdata.url)
        assert hp.homepage_isvisible(), \
            "Homepage is not visible. Some elements are missing, or webpage title is not 'Automation Exercise'"
        ap = hp.click_products_btn()
        ap.add_product_to_cart(0)
        ap.click_continue_shopping_btn()
        ap.add_product_to_cart(0)
        ap.click_continue_shopping_btn()
        ap.add_product_to_cart(3)
        cp = ap.click_view_cart_btn()
        
        added_list = ap.get_products_added_in_cart()
        actual_list = cp.get_cart_items()
        
        for i in range(len(added_list)):
            actual_product_description = list(added_list[i].keys())[0]
            cart_product_description = list(actual_list[i].keys())[0]
            actual_product_price = added_list[i][actual_product_description]['price']
            cart_product_price = actual_list[i][actual_product_description]['price']
            actual_product_quantity = added_list[i][actual_product_description]['quantity']
            cart_product_quantity = actual_list[i][actual_product_description]['quantity']
            actual_product_total_price = actual_product_price * actual_product_quantity
            cart_product_total_price = actual_list[i][actual_product_description]['total_price']
            
            assert actual_product_description == cart_product_description, \
                "Description is not matched"
            assert actual_product_price == cart_product_price, \
                "Price is not matched"
            assert actual_product_quantity == cart_product_quantity, \
                "Quantity is not matched"
            assert actual_product_total_price == cart_product_total_price, \
                "Total Price is not matched"

        
        
        
        
            
            
            
            