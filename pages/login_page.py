from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/"
    
    # --- Locators ---
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
  
 
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

   