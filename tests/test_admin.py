import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

# COMMON FIXTURE 

@pytest.fixture
def logged_in_admin(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    
    WebDriverWait(driver, 20).until(
        EC.url_contains("dashboard")
    )
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_panel()
    return admin_page

# USER MANAGEMENT TESTS

def test_add_and_verify_new_user(logged_in_admin):
  
    admin_page = logged_in_admin
    unique_username = f"User{int(time.time())}" 
    
    admin_page.click_add_user()
    assert "saveSystemUser" in admin_page.get_current_url()
    
    admin_page.create_new_user(
        role="ESS",
        employee_name="a", 
        username=unique_username,
        password="Secure#Pass_2026!",
        status="Enabled"
    )
    
    assert "viewSystemUsers" in admin_page.get_current_url()
    admin_page.search_user_by_username(unique_username)
    assert "Found" in admin_page.get_records_text()
    assert admin_page.get_first_row_username() == unique_username

def test_search_existing_user(logged_in_admin):
   
    admin_page = logged_in_admin
    search_query = "Admin"
    
    admin_page.search_user_by_username(search_query)
    assert "Found" in admin_page.get_records_text()
    assert admin_page.get_first_row_username() == search_query

def test_search_invalid_user(logged_in_admin):
    admin_page = logged_in_admin
    search_query = "FakeUserXYZ99"
    
    admin_page.search_user_by_username(search_query)
    assert "No Records Found" in admin_page.get_records_text()