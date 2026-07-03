from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Login_with_valid_credentials(driver):
    loginpage = LoginPage(driver)
    loginpage.load()
    loginpage.login("Admin", "admin123")
    assert "dashboard" in driver.current_url

def test_login_with_invalid_credentials(driver):
    loginpage = LoginPage(driver)
    loginpage.load()
    loginpage.login("Admin", "admin1234")
    assert "dashboard" not in driver.current_url
   
