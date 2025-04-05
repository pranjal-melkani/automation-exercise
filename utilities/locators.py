from selenium.webdriver.common.by import By


class Homepage_locators:
    home_slider = (By.ID, "slider")
    

class Signup_Login_page_locators:
    # Signup
    signup_form = (By.CLASS_NAME, "signup-form")
    signup_header = (By.XPATH, "//*[text()='New User Signup!']")
    signup_name_field = (By.XPATH, "//*[@data-qa='signup-name']")
    signup_email_field = (By.XPATH, "//*[@data-qa='signup-email']")
    signup_btn = (By.XPATH, "//*[@data-qa='signup-button']")
    
    enter_account_info_header = (By.XPATH, "//*[text()='Enter Account Information']")
    title_mr = (By.ID, "id_gender1")
    title_mrs = (By.ID, "id_gender2")
    password_field = (By.ID, "password")
    dob_day_field = (By.ID, "days")
    dob_month_field = (By.ID, "months")
    dob_year_field = (By.ID, "years")
    newsletter_checkbox = (By.ID, "newsletter")
    special_offer_checkbox = (By.ID, "optin")
    first_name_field = (By.ID, "first_name")
    last_name_field = (By.ID, "last_name")
    company_field = (By.ID, "company")
    address1_field = (By.ID, "address1")
    address2_field = (By.ID, "address2")
    country_dropdown = (By.ID, "country")
    state_field = (By.ID, "state")
    city_field = (By.ID, "city")
    zipcode_field = (By.ID, "zipcode")
    mobile_no_field = (By.ID, "mobile_number")
    create_account_btn = (By.XPATH, "//*[@data-qa='create-account']")
    
    account_created_message = (By.XPATH, "//*[text()='Account Created!']")
    continue_btn = (By.XPATH, "//*[@data-qa='continue-button']")
    delete_account_btn = (By.XPATH, "//*[contains(text(), 'Delete Account')]")
    account_deleted_message = (By.XPATH, "//*[text()='Account Deleted!']")
    email_exists_error_msg = (By.XPATH, "//*[text()='Email Address already exist!']")
    
    # Login
    login_form = (By.CLASS_NAME, "login-form")
    login_header = (By.XPATH, "//*[text()='Login to your account']")
    login_email_field = (By.XPATH, "//*[@data-qa='login-email']")
    login_password_field = (By.XPATH, "//*[@data-qa='login-password']")
    login_btn = (By.XPATH, "//*[@data-qa='login-button']")
    incorrect_credentials_error_msg = (By.XPATH, "//*[text()='Your email or password is incorrect!']")


class Contactus_page_locators:
    get_in_touch_text = (By.XPATH, "//*[text()='Get In Touch']")
    name_field = (By.XPATH, "//*[@data-qa='name']")
    email_field = (By.XPATH, "//*[@data-qa='email']")
    subject_field = (By.XPATH, "//*[@data-qa='subject']")
    message_field = (By.ID, "message")
    file_upload_field = (By.NAME, "upload_file")
    submit_btn = (By.XPATH, "//*[@data-qa='submit-button']")
    success_message = (By.XPATH, "//*[@class='contact-form']//*[text()=\
                       'Success! Your details have been submitted successfully.']")
    home_btn = (By.XPATH, "//*[@id='form-section']//*[contains(text(), 'Home')]")
    

class Testcases_page_locators:
    testcases_text = (By.XPATH, "//*[text()='Test Cases']")
    

class AllProducts_page_locators:
    all_products_text = (By.XPATH, "//*[text()='All Products']") 
    single_product = (By.CLASS_NAME, "single-products")
    view_product_link = (By.XPATH, "//*[text()='View Product']")
    

class Product_Details_page_locators:
    product_name = (By.XPATH, "//*[@class='product-information']//h2")
    product_category = (By.XPATH, "//*[@class='product-information']//p[1]")
    product_availability = (By.XPATH, "//*[@class='product-information']//p[2]")
    product_condition = (By.XPATH, "//*[@class='product-information']//p[3]")
    product_brand = (By.XPATH, "//*[@class='product-information']//p[4]")
    
    
    
    
    
    