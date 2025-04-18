import pytest
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True, params=['chrome'])
def driver(request):
    browser = request.param
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception("Please check the browser type")
    
    driver.maximize_window()
    yield driver
    driver.quit()