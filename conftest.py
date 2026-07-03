
import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--password-store=basic")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()