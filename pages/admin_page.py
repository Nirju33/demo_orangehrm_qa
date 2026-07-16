import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AdminPage(BasePage):
    
    def get_current_url(self):
        return self.driver.current_url

    # ==========================================
    # COMMON LOCATORS 
    # ==========================================
    ADMIN_MENU_BUTTON = (By.XPATH, "//a[span[text()='Admin']]")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit' and contains(., 'Save')]")
    
    # ==========================================
    # USER MANAGEMENT LOCATORS
    # ==========================================
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
    
    # ==========================================
    # JOB MANAGEMENT & PAY GRADES LOCATORS
    # ==========================================
    JOB_MENU = (By.XPATH, "//span[contains(text(), 'Job') and @class='oxd-topbar-body-nav-tab-item']")
    JOB_TITLES_OPTION = (By.XPATH, "//ul[@class='oxd-dropdown-menu']/li/a[text()='Job Titles']")
    PAY_GRADES_OPTION = (By.XPATH, "//ul[@class='oxd-dropdown-menu']/li/a[text()='Pay Grades']")
    
    JOB_TITLE_INPUT = (By.XPATH, "//div[label[text()='Job Title']]/following-sibling::div/input")
    JOB_DESC_TEXTAREA = (By.XPATH, "//div[label[text()='Job Description']]/following-sibling::div/textarea")
    JOB_NOTE_TEXTAREA = (By.XPATH, "//div[label[text()='Note']]/following-sibling::div/textarea")
    JOB_SPECIFICATION_INPUT = (By.XPATH, "//input[@type='file']")
    
    PAY_GRADE_NAME_INPUT = (By.XPATH, "//div[label[text()='Name']]/following-sibling::div/input")
    
    # CURRENCY BOX LOCATORS
    CURRENCY_SECTION_ADD_BUTTON = (By.XPATH, "//h6[text()='Currencies']/following-sibling::button[contains(., 'Add')]")
    CURRENCY_DROPDOWN = (By.XPATH, "//div[label[text()='Currency']]/following-sibling::div//div[@class='oxd-select-text-input']")
    MIN_SALARY_INPUT = (By.XPATH, "//div[label[text()='Minimum Salary']]/following-sibling::div/input")
    MAX_SALARY_INPUT = (By.XPATH, "//div[label[text()='Maximum Salary']]/following-sibling::div/input")
    CURRENCY_SAVE_BUTTON = (By.XPATH, "//h6[text()='Add Currency']/following-sibling::form//button[@type='submit' and contains(., 'Save')]")
    # METHODS
    # ==========================================
    def navigate_to_admin_panel(self):
        self.click(self.ADMIN_MENU_BUTTON)
        self.wait_for_url_contains("admin/viewSystemUsers")

    def click_add(self):
        self.click(self.ADD_BUTTON)

    def save_form(self):
        self.click(self.SAVE_BUTTON)
        time.sleep(2) 
        
    def create_new_user(self, role, employee_name, username, password, status="Enabled"):
        self.click(self.USER_ROLE_DROPDOWN)
        role_locator = (By.XPATH, f"//div[@role='listbox']//span[text()='{role}']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(role_locator)).click()
        time.sleep(0.5)
    
        el = self.find_visible(self.EMPLOYEE_NAME_INPUT)
        el.click()
        el.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        el.send_keys(employee_name)
        
        dropdown_option = (By.XPATH, "//div[@role='listbox']//span")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(dropdown_option))
        
        el.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        el.send_keys(Keys.ENTER)
        time.sleep(1) 
        
        self.click(self.STATUS_DROPDOWN)
        time.sleep(0.5)
        
        status_locator = (By.XPATH, f"//div[@role='listbox']//span[text()='{status}']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(status_locator)).click()
        time.sleep(0.5)
    
        self.type(self.NEW_USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.type(self.CONFIRM_PASSWORD_INPUT, password)
        time.sleep(1)

        self.save_form()
        WebDriverWait(self.driver, 25).until(EC.url_contains("admin/viewSystemUsers"))

    def search_user_by_username(self, username):
        el = self.find_visible(self.SEARCH_USERNAME_INPUT)
        el.click()
        el.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        el.send_keys(username)
        
        self.click(self.SEARCH_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.RECORDS_FOUND_LABEL))
        time.sleep(1)

    def get_records_text(self):
        return self.find_visible(self.RECORDS_FOUND_LABEL).text

    def get_first_row_username(self):
        return self.find_visible(self.FIRST_ROW_USERNAME_CELL).text
    
    def navigate_to_job_titles(self):
        self.click(self.JOB_MENU)
        self.click(self.JOB_TITLES_OPTION)
        self.wait_for_url_contains("admin/viewJobTitleList")
    
    def create_new_job_title(self, title, description, file_path, note):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.JOB_TITLE_INPUT)).send_keys(title)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.JOB_DESC_TEXTAREA)).send_keys(description)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.JOB_SPECIFICATION_INPUT)).send_keys(file_path)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.JOB_NOTE_TEXTAREA)).send_keys(note)

        save_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_btn.click()
    
    def navigate_to_pay_grades(self):
        self.click(self.JOB_MENU)
        self.click(self.PAY_GRADES_OPTION)
        self.wait_for_url_contains("admin/viewPayGrades")

    def create_pay_grade_name(self, grade_name):
        """सुरुमा Pay Grade को नाम मात्र राखेर Save गर्ने"""
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PAY_GRADE_NAME_INPUT))
        el.send_keys(grade_name)
        
        first_save_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        first_save_btn.click()
        time.sleep(3)
        
    def add_currency_to_grade(self, currency_name, min_salary, max_salary):
        """Currencies को + Add बटन थिचेर Topbar ले नछोपिने गरी विवरण भर्ने र Save गर्ने"""
        # १. पेज लोड हुन निश्चित गर्ने
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("payGrade")
        )
        time.sleep(2)

        # २. 'Currencies' सेक्सनको '+ Add' बटन खोज्ने र स्क्रोल गरेर क्लिक गर्ने
        add_currency_btn = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.CURRENCY_SECTION_ADD_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_currency_btn)
        time.sleep(0.5)
        
        try:
            add_currency_btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", add_currency_btn)
            
        # फारम विस्तार (open) हुन थोरै समय पर्खिने
        time.sleep(1.5)

        # ३. Currency ड्रपडाउन खोज्ने
        dropdown = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.CURRENCY_DROPDOWN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", dropdown)
        time.sleep(1.5)
        
        # ४. लिस्टबाट सही Currency छान्ने
        currency_option = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//*[contains(text(), '{currency_name}')]"))
        )
        currency_option.click()
        time.sleep(1)
        
        # ५. Minimum Salary भर्ने
        min_el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.MIN_SALARY_INPUT))
        min_el.click()
        min_el.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        min_el.send_keys(min_salary)
        
        # ६. Maximum Salary भर्ने
        max_el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.MAX_SALARY_INPUT))
        max_el.click()
        max_el.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        max_el.send_keys(max_salary)
        
        # ७. मुद्रा फारमको Save बटन खोज्ने र JS Click मार्फत क्लिक गर्ने
        save_btn = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.CURRENCY_SAVE_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", save_btn)
        time.sleep(3)