import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AdminPage(BasePage):
    
    def get_current_url(self):
        return self.driver.current_url
        
    
    #  LOCATORS 

    ADMIN_MENU_BUTTON = (By.XPATH, "//a[span[text()='Admin']]")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit' and contains(., 'Save')]")

    SEARCH_USERNAME_INPUT = (By.XPATH, "//div[label[text()='Username']]/following-sibling::div/input")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit' and contains(., 'Search')]")
    RECORDS_FOUND_LABEL = (By.XPATH, "//span[contains(., 'Found')]")
    FIRST_ROW_USERNAME_CELL = (By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[2]/div")
    
    USER_ROLE_DROPDOWN = (By.XPATH, "//div[label[text()='User Role']]/following-sibling::div//div[@class='oxd-select-text-input']")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//div[label[text()='Employee Name']]/following-sibling::div//input")
    STATUS_DROPDOWN = (By.XPATH, "//div[label[text()='Status']]/following-sibling::div//div[@class='oxd-select-text-input']")
    NEW_USERNAME_INPUT = (By.XPATH, "//div[label[text()='Username']]/following-sibling::div/input")
    PASSWORD_INPUT = (By.XPATH, "//div[label[text()='Password']]/following-sibling::div/input")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//div[label[text()='Confirm Password']]/following-sibling::div/input")
    
    JOB_MENU = (By.XPATH, "//span[contains(text(), 'Job') and @class='oxd-topbar-body-nav-tab-item']")
    JOB_TITLES_OPTION = (By.XPATH, "//ul[@class='oxd-dropdown-menu']/li/a[text()='Job Titles']")
    JOB_TITLE_INPUT = (By.XPATH, "//div[label[text()='Job Title']]/following-sibling::div/input")
    JOB_DESC_TEXTAREA = (By.XPATH, "//div[label[text()='Job Description']]/following-sibling::div/textarea")
    JOB_NOTE_TEXTAREA = (By.XPATH, "//div[label[text()='Note']]/following-sibling::div/textarea")

    # २. COMMON ACTIONS 

    def navigate_to_admin_panel(self):
        self.click(self.ADMIN_MENU_BUTTON)
        self.wait_for_url_contains("admin/viewSystemUsers")

    def click_add(self):
        self.click(self.ADD_BUTTON)

    def save_form(self):
        self.click(self.SAVE_BUTTON)
        time.sleep(1.5) 
        
    # USER MANAGEMENT ACTIONS

    def create_new_user(self, role, employee_name, username, password, status="Enabled"):
        self.click(self.USER_ROLE_DROPDOWN)
        time.sleep(0.5)
        self.click((By.XPATH, f"//div[@role='listbox']//span[text()='{role}']"))
        time.sleep(0.5)
    
        el = self.find_visible(self.EMPLOYEE_NAME_INPUT)
        el.click()
        el.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        el.send_keys(employee_name)
        time.sleep(2.5) 

        el.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        el.send_keys(Keys.ENTER)
        time.sleep(1) 
        
        self.click(self.STATUS_DROPDOWN)
        time.sleep(0.5)
        self.click((By.XPATH, f"//div[@role='listbox']//span[text()='{status}']"))
        time.sleep(0.5)
    
        self.type(self.NEW_USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.type(self.CONFIRM_PASSWORD_INPUT, password)
        time.sleep(1)

        self.save_form()
  
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("admin/viewSystemUsers")
        )

    def search_user_by_username(self, username):
        el = self.find_visible(self.SEARCH_USERNAME_INPUT)
        el.click()
        el.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        el.send_keys(username)
        
        self.click(self.SEARCH_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.RECORDS_FOUND_LABEL)
        )
        time.sleep(1)

    def get_records_text(self):
        return self.find_visible(self.RECORDS_FOUND_LABEL).text

    def get_first_row_username(self):
        return self.find_visible(self.FIRST_ROW_USERNAME_CELL).text
    
    #  JOB TITLE ACTIONS
    def navigate_to_job_titles(self):
        self.click(self.JOB_MENU)
        self.click(self.JOB_TITLES_OPTION)
        self.wait_for_url_contains("admin/viewJobTitleList")

    def create_new_job_title(self, title, description=None, note=None):
        self.type(self.JOB_TITLE_INPUT, title)
        
        if description:
            self.type(self.JOB_DESC_TEXTAREA, description)
        if note:
            self.type(self.JOB_NOTE_TEXTAREA, note)
            
        self.save_form()
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("admin/viewJobTitleList")
        )