from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_service = Service(ChromeDriverManager().install())  # This will use the latest version by default
driver = webdriver.Chrome(service=chrome_service)

wait = WebDriverWait(driver, 10)

class BaseObject:
    def __init__(self, driver: Chrome, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

