import time
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

def test_Login_with_empty_credentials(driver):
    loginpage = LoginPage(driver)
    loginpage.load()
    loginpage.login("", "")
    assert "dashboard" not in driver.current_url

def test_login_with_blank_username(driver):
    loginpage = LoginPage(driver)
    loginpage.load()
    loginpage.login("", "admin123")
    assert "dashboard" not in driver.current_url

def test_login_with_blank_password(driver):
    loginpage = LoginPage(driver)
    loginpage.load()
    loginpage.login("Admin", "")
    assert "dashboard" not in driver.current_url

def test_login_with_special_characters(driver):
    loginpage = LoginPage(driver)
    loginpage.load()
    loginpage.login("Admin!@#", "admin123")
    assert "dashboard" not in driver.current_url

def test_login_with_long_username(driver):
    loginpage = LoginPage(driver)
    loginpage.load()
    long_username = "A" * 256  # 256 characters long
    loginpage.login(long_username, "admin123")
    assert "dashboard" not in driver.current_url


    time.sleep(10)