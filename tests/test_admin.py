import pytest
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

# ==========================================
# COMMON FIXTURE
# ==========================================
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

# ==========================================
# USER MANAGEMENT TESTS
# ==========================================
def test_add_and_verify_new_user(logged_in_admin):
    admin_page = logged_in_admin
    unique_username = f"User{int(time.time())}" 
    admin_page.click_add()
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

# ==========================================
# JOB TITLE TEST
# ==========================================
def test_add_job_title(logged_in_admin):
    admin_page = logged_in_admin
    admin_page.navigate_to_job_titles()
    admin_page.click_add()
    unique_job = f"QA Automation {int(time.time())}"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dummy_file_path = os.path.join(current_dir, "temp_job_spec.png")
    
    # Create temp file
    if not os.path.exists(dummy_file_path):
        with open(dummy_file_path, "wb") as f:
            f.write(b"") 
            
    try:
        admin_page.create_new_job_title(
            title=unique_job,
            description="Responsible for writing robust automation tests.",
            file_path=dummy_file_path,  
            note="Created via automated script."
        )
        WebDriverWait(admin_page.driver, 15).until(
            EC.url_contains("viewJobTitleList")
        )
        assert "viewJobTitleList" in admin_page.get_current_url()
        
    finally:
        # Delete temp file
        if os.path.exists(dummy_file_path):
            os.remove(dummy_file_path)
            
    time.sleep(1)
    
# ==========================================
# PAY GRADE TEST
# ==========================================
def test_add_pay_grade_and_currency(logged_in_admin):
    admin_page = logged_in_admin
    admin_page.navigate_to_pay_grades()
    admin_page.click_add()
    unique_grade = f"Grade {int(time.time())}"
    admin_page.create_pay_grade_name(unique_grade)
    WebDriverWait(admin_page.driver, 15).until(
        EC.url_contains("payGrade")
    )
    admin_page.wait_for_spinner_to_disappear()
    admin_page.add_currency_to_grade(
        currency_name="United States Dollar",
        min_salary="15000",
        max_salary="30000"
    )
    current_url = admin_page.get_current_url()
    assert "payGrade" in current_url or "viewPayGrades" in current_url
    
    # Employment status

def test_add_employment_status(logged_in_admin):
    admin_page = logged_in_admin
    admin_page.navigate_to_employment_status()
    admin_page.click_add()
    status_name = "Internship"
    admin_page.create_employment_status(status_name)
    
    assert "employmentStatus" in admin_page.get_current_url()