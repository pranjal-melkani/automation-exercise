from pages.homepage import Homepage
from utilities.testdata import Testdata


class TestProducts:
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
        
            
            
            
            
            