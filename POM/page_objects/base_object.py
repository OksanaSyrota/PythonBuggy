from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Corrected driver initialization
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 10)

class BaseObject:
    def __init__(self, driver: Chrome, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

