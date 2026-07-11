import pytest
import time
from pages.login_page import LoginPage
from pages.admin_page import AdminPage  

# =========================================================================
# OLD CODE: EXISTING USER MANAGEMENT TESTS (तिम्रो पुरानो टेस्टहरू)
# =========================================================================

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


# =========================================================================
# 🆕 NEW CODE: JOB DROPDOWN OPTIONS TESTS (यो नयाँ थपिएको हो)
# =========================================================================

def test_admin_add_job_title(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(4)
    LoginPage(driver).login("Admin", "admin123")
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_module()
    
    admin_page.open_job_dropdown_option("Job Titles")
    
    unique_title = f"QA_Engineer_{int(time.time())}"
    admin_page.fill_and_save_standard_form(unique_title, "Writes automation code.")
    
    assert unique_title in driver.page_source


def test_admin_add_pay_grade(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(4)
    LoginPage(driver).login("Admin", "admin123")
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_module()
    
    admin_page.open_job_dropdown_option("Pay Grades")
    
    unique_grade = f"Grade_{int(time.time())}"
    admin_page.fill_and_save_standard_form(unique_grade)
    
    assert unique_grade in driver.page_source


def test_admin_add_employment_status(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(4)
    LoginPage(driver).login("Admin", "admin123")
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_module()
    
    admin_page.open_job_dropdown_option("Employment Status")
    
    unique_status = f"Status_{int(time.time())}"
    admin_page.fill_and_save_standard_form(unique_status)
    
    assert unique_status in driver.page_source


def test_admin_add_job_category(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(4)
    LoginPage(driver).login("Admin", "admin123")
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_module()
    
    admin_page.open_job_dropdown_option("Job Categories")
    
    unique_category = f"Category_{int(time.time())}"
    admin_page.fill_and_save_standard_form(unique_category)
    
    assert unique_category in driver.page_source


def test_admin_add_work_shift(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(4)
    LoginPage(driver).login("Admin", "admin123")
    
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_module()
    
    admin_page.open_job_dropdown_option("Work Shifts")
    
    admin_page.click(admin_page.add_button)
    time.sleep(2)
    
    unique_shift = f"Shift_{int(time.time())}"
    shift_name_field = driver.find_element("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    shift_name_field.send_keys(unique_shift)
    
    admin_page.click(admin_page.save_button)
    time.sleep(4)
    
    assert unique_shift in driver.page_source