import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class AdminPage(BasePage):
    
    def get_current_url(self):
        return self.driver.current_url
        
    ADMIN_MENU_BUTTON = (By.XPATH, "//a[span[text()='Admin']]")
    
    SEARCH_USERNAME_INPUT = (By.XPATH, "//div[label[text()='Username']]/following-sibling::div/input")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit' and contains(., 'Search')]")
    ADD_BUTTON = (By.XPATH, "//button[contains(., 'Add')]")
    RECORDS_FOUND_LABEL = (By.XPATH, "//span[contains(., 'Records Found') or contains(., 'Record Found')]")
    FIRST_ROW_USERNAME_CELL = (By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[2]/div")
    
    USER_ROLE_DROPDOWN = (By.XPATH, "//div[label[text()='User Role']]/following-sibling::div//div[@class='oxd-select-text-input']")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//div[label[text()='Employee Name']]/following-sibling::div//input")
    EMPLOYEE_AUTOCOMPLETE_OPTION = (By.XPATH, "//div[@role='listbox']//div[@role='option']")
    STATUS_DROPDOWN = (By.XPATH, "//div[label[text()='Status']]/following-sibling::div//div[@class='oxd-select-text-input']")
    
    NEW_USERNAME_INPUT = (By.XPATH, "//div[label[text()='Username']]/following-sibling::div/input")
    PASSWORD_INPUT = (By.XPATH, "//div[label[text()='Password']]/following-sibling::div/input")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//div[label[text()='Confirm Password']]/following-sibling::div/input")
    
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit' and contains(., 'Save')]")
    CANCEL_BUTTON = (By.XPATH, "//button[@type='button' and contains(., 'Cancel')]")
    
    SUCCESS_TOAST = (By.XPATH, "//div[@id='oxd-toast-container']//p[contains(@class, 'oxd-text--toast-title')]")

    def navigate_to_admin_panel(self):
        self.click(self.ADMIN_MENU_BUTTON)
        self.wait_for_url_contains("admin/viewSystemUsers")

    def click_add_user(self):
        self.click(self.ADD_BUTTON)
        self.wait_for_url_contains("admin/saveSystemUser")

    def select_user_role(self, role_name):
        self.click(self.USER_ROLE_DROPDOWN)
        option_locator = (By.XPATH, f"//div[@role='listbox']//span[text()='{role_name}']")
        self.click(option_locator)

    def enter_employee_name(self, partial_name):
        el = self.find_visible(self.EMPLOYEE_NAME_INPUT)
        el.click()
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.BACKSPACE)
        el.send_keys(partial_name)
        time.sleep(3)
        dropdown_option = self.find_visible(self.EMPLOYEE_AUTOCOMPLETE_OPTION, timeout=10)
        dropdown_option.click()
        el.send_keys(Keys.ENTER)
        time.sleep(1)

    def select_status(self, status_value):
        self.click(self.STATUS_DROPDOWN)
        option_locator = (By.XPATH, f"//div[@role='listbox']//span[text()='{status_value}']")
        self.click(option_locator)

    def create_new_user(self, role, employee_name, username, password, status="Enabled"):
        self.select_user_role(role)
        self.enter_employee_name(employee_name)
        self.select_status(status)
        self.type(self.NEW_USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.type(self.CONFIRM_PASSWORD_INPUT, password)
        time.sleep(2)
        self.click(self.SAVE_BUTTON)
        self.wait_for_url_contains("admin/viewSystemUsers")

    def search_user_by_username(self, username):
        self.type(self.SEARCH_USERNAME_INPUT, username)
        self.click(self.SEARCH_BUTTON)
        time.sleep(2)

    def get_records_text(self):
        return self.find_visible(self.RECORDS_FOUND_LABEL).text

    def get_first_row_username(self):
        return self.find_visible(self.FIRST_ROW_USERNAME_CELL).text

    def is_success_toast_displayed(self):
        try:
            text = self.find_visible(self.SUCCESS_TOAST, timeout=7).text
            return "Success" in text
        except:
            return False