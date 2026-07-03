from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/"
    
    # --- Login Page Locators ---
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
    
    # --- Reset Password Page Locators ---
    RESET_USERNAME_INPUT = (By.NAME, "username")
    RESET_BUTTON = (By.XPATH, "//button[contains(@class, 'orangehrm-forgot-password-button--reset')]") 

    def load(self):
        self.open(self.URL)
        self._wait_for_page_ready()
       
    def _wait_for_page_ready(self):
        self.find_visible(self.USERNAME_INPUT)
        self.find_visible(self.PASSWORD_INPUT)
        self.find_visible(self.LOGIN_BUTTON)
        
    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

   