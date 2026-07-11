import pytest
import time
from pages.login_page import LoginPage
from pages.admin_page import AdminPage  
def test_admin_add_and_search_valid_user(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(4)
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    time.sleep(3)
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_module()
    time.sleep(3)
    
    unique_username = f"QA_User_{int(time.time())}"
    admin_page.add_new_user("a", unique_username, "Password@123")
    time.sleep(6)  
    
    admin_page.search_user_by_username(unique_username)
    time.sleep(3)
    
    results = admin_page.get_search_results()
    assert "Record Found" in results



def test_admin_search_existing_system_user(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(4)
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    time.sleep(3)
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_module()
    time.sleep(3)
    
    admin_page.search_user_by_username("Admin")
    time.sleep(3)
    
    results = admin_page.get_search_results()
    assert "Record Found" in results


def test_admin_search_invalid_user_no_records(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(4)
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    time.sleep(3)
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_module()
    time.sleep(3)
    
    admin_page.search_user_by_username("FakeUser_DoesNotExist_1234")
    time.sleep(3)
    
    results = admin_page.get_search_results()
    assert "No Records Found" in results


def test_admin_reset_search_filter_clears_input(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(4)
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    time.sleep(3)
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_module()
    time.sleep(3)
    
    admin_page.type(admin_page.search_username_input, "ResetValueText")
    time.sleep(1)
    
    reset_button = driver.find_element("xpath", "//button[contains(., 'Reset')]")
    reset_button.click()
    time.sleep(2)
    
    current_input_value = driver.find_element(*admin_page.search_username_input).get_attribute("value")
    assert current_input_value == ""