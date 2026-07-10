import pytest
import time
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

@pytest.fixture(autouse=True)
def setup_and_login(driver):
    """Sabae test vanda pahile automatic login garera Admin module ma puryaune fixture"""
    # LoginPage ko open_page hatayera sidhai driver bat URL kholne
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3) # Page loading time ko lagi
    
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    time.sleep(2)
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_module()
    time.sleep(2) # Page stable huna ko lagi

# -------------------------------------------------------------------------
# TEST 1: New User Add garne ra Verify garne (Happy Path)
# -------------------------------------------------------------------------
def test_add_and_search_valid_user(driver):
    admin_page = AdminPage(driver)
    unique_username = f"QA_User_{int(time.time())}"
    
    admin_page.add_new_user(
        emp_search_key="a", 
        unique_username=unique_username, 
        password="Password@123"
    )
    time.sleep(5)
    
    admin_page.search_user_by_username(unique_username)
    time.sleep(2)
    
    results = admin_page.get_search_results()
    assert "Record Found" in results or "1" in results, f"Expected 1 record found but got: {results}"

# -------------------------------------------------------------------------
# TEST 2: Existing User Search gari verification garne 
# -------------------------------------------------------------------------
def test_search_existing_admin_user(driver):
    admin_page = AdminPage(driver)
    admin_page.search_user_by_username("Admin")
    time.sleep(2)
    
    results = admin_page.get_search_results()
    assert "Record Found" in results, f"Default Admin user search fail vayo! Got: {results}"

# -------------------------------------------------------------------------
# TEST 3: System ma navako (Invalid) User Search test 
# -------------------------------------------------------------------------
def test_search_invalid_user_should_return_no_records(driver):
    admin_page = AdminPage(driver)
    admin_page.search_user_by_username("NonExistingUser_9999")
    time.sleep(2)
    
    results = admin_page.get_search_results()
    assert "No Records Found" in results, f"Expected 'No Records Found' text but got: {results}"

# -------------------------------------------------------------------------
# TEST 4: Input Reset Button functionally checker
# -------------------------------------------------------------------------
def test_reset_search_filter(driver):
    admin_page = AdminPage(driver)
    admin_page.type(admin_page.search_username_input, "TemporaryText")
    
    reset_button = driver.find_element("xpath", "//button[contains(., 'Reset')]")
    reset_button.click()
    time.sleep(1)
    
    current_input_value = driver.find_element(*admin_page.search_username_input).get_attribute("value")
    assert current_input_value == "", "Reset button click garda pani text clear vayena!"