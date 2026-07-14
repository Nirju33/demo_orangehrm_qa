
import pytest
import time
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

@pytest.fixture
def logged_in_admin(driver):
    """Fixture to log in and automatically navigate to the Admin System Users page."""
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    
    assert "dashboard" in driver.current_url
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_panel()
    return admin_page


def test_add_and_verify_new_user(logged_in_admin):
    """
    Flow: 
    1. Navigate to Add User page (saveSystemUser)
    2. Fill out and submit the form
    3. Verify redirection back to the System Users list (viewSystemUsers)
    4. Search and verify the newly added user
    """
    admin_page = logged_in_admin
    unique_username = f"User{int(time.time())}" 
    
    # 1. Click Add button and verify page change
    admin_page.click_add_user()
    assert "saveSystemUser" in admin_page.get_current_url()
    
    # 2. Create the user
    admin_page.create_new_user(
        role="Admin",
        employee_name=" John Pham", 
        username=unique_username,
        password="Password123!",
        status="Enabled"
    )
    
    # 3. Verify page automatically returned back to the list screen
    assert "viewSystemUsers" in admin_page.get_current_url()
    
    # 4. Search and confirm the user exists in the grid
    admin_page.search_user_by_username(unique_username)
    
    assert "Record Found" in admin_page.get_records_text()
    assert admin_page.get_first_row_username() == unique_username


def test_search_existing_user(logged_in_admin):
    """Test searching for the default administrative user."""
    admin_page = logged_in_admin
    search_query = "Admin"
    
    admin_page.search_user_by_username(search_query)
    
    assert "Record Found" in admin_page.get_records_text()
    assert admin_page.get_first_row_username() == search_query


def test_search_invalid_user(logged_in_admin):
    """Test searching for a non-existent username."""
    admin_page = logged_in_admin
    search_query = "FakeUserXYZ99"
    
    admin_page.search_user_by_username(search_query)
    
    assert "No Records Found" in admin_page.get_records_text()