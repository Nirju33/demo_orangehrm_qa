import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage  

class AdminPage(BasePage): 
    def __init__(self, driver):
        super().__init__(driver)  

        # --- Side Menu ---
        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        
        # --- Search Filter Section Locators ---
        self.search_username_input = (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters']//input")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.records_found_text = (By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span")
        
        # --- Add User Form Section Locators ---
        self.add_button = (By.XPATH, "//button[contains(., 'Add')]")
        self.user_role_dropdown = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
        self.admin_option = (By.XPATH, "//div[@role='listbox']//*[text()='Admin']")
        
        self.employee_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.employee_dropdown_option = (By.XPATH, "//div[@role='listbox']//div[@role='option']")
        
        self.status_dropdown = (By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
        self.enabled_option = (By.XPATH, "//div[@role='listbox']//*[text()='Enabled']")
        
        self.username_field = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.password_field = (By.XPATH, "(//input[@type='password'])[1]")
        self.confirm_password_field = (By.XPATH, "(//input[@type='password'])[2]")
        self.save_button = (By.XPATH, "//button[@type='submit']")

    def navigate_to_admin_module(self):
        self.click(self.admin_menu)  

    def add_new_user(self, emp_search_key, unique_username, password):
        self.click(self.add_button)
        time.sleep(2) 
        
        self.click(self.user_role_dropdown)
        time.sleep(1)
        self.click(self.admin_option)
        
        self.type(self.employee_input, emp_search_key)
        time.sleep(3)  
        self.click(self.employee_dropdown_option)
        
        self.click(self.status_dropdown)
        time.sleep(1)
        self.click(self.enabled_option)
        
        self.type(self.username_field, unique_username)
        self.type(self.password_field, password)
        self.type(self.confirm_password_field, password)
        
        time.sleep(1)
        self.click(self.save_button)

    def search_user_by_username(self, username):
        element = self.find(self.search_username_input)
        element.clear()
        self.type(self.search_username_input, username)
        self.click(self.search_button)

    def get_search_results(self):
        element = self.find_visible(self.records_found_text)
        return element.text