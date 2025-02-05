import random
import string
import uuid
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located

from POM.page_objects.base_object import BaseObject
from selenium.webdriver.common.by import By


locators = {
#Start Page
    'RegisterButtonStartPage': (By.CSS_SELECTOR, 'a[href="/register"]'),
    'LogoOfTheSite': (By.CSS_SELECTOR, '.navbar-brand'),
    'UsernameField': (By.CSS_SELECTOR, '#username'),
    'FirstNameField': (By.CSS_SELECTOR, '#firstName'),
    'LastNameField': (By.CSS_SELECTOR, '#lastName'),
    'PasswordField': (By.CSS_SELECTOR, '#password'),
    'ConfirmPasswordField': (By.CSS_SELECTOR, '#confirmPassword'),
    'RegisterButton': (By.XPATH, '//*[@class="container my-form"]/div/form/button'),
    'CancelButton': (By.XPATH, '//*[@class="container my-form"]/div/form/a'),
    'TextAfterRegister': (By.XPATH, '//*[@class="container my-form"]/div/form/div[6]'),
    'PasswordDoNotMatchText': (By.XPATH, '//*[@class="container my-form"]/div/form/div[5]/div[1]'),
}

class RegisterPage(BaseObject):

    #Open Register Page
    def open_register_page(self):
        self.driver.get('http://buggy.justtestit.org/')
        self.wait.until(element_to_be_clickable(locators['RegisterButtonStartPage']))
        self.driver.find_element(*locators['RegisterButtonStartPage']).click()
        self.wait.until(visibility_of_element_located(locators['UsernameField']))

    #Enter Valid Data in the Register Form
    def enter_user_name(self):
        user_name = f"user_{uuid.uuid4().hex[:8]}" #generate dynamic username
        self.driver.find_element(*locators['UsernameField']).send_keys(user_name)

    def enter_first_name(self):
        first_name = f"user_{uuid.uuid4().hex[:8]}"
        self.driver.find_element(*locators['FirstNameField']).send_keys(first_name)

    def enter_last_name(self):
        last_name = f"user_{uuid.uuid4().hex[:8]}"
        self.driver.find_element(*locators['LastNameField']).send_keys(last_name)

    def enter_password_and_confirm_password(self):
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        #return at least one letter, one number, one symbol
        password = [random.choice(string.ascii_letters), random.choice(string.digits), random.choice(symbols)]
        password += random.choices((string.ascii_letters + string.digits + symbols), k = 5)
        random.shuffle(password) #Shuffle to randomize the order
        password = ''.join(password) #convert list to string
        self.driver.find_element(*locators['PasswordField']).send_keys(password)
        self.driver.find_element(*locators['ConfirmPasswordField']).send_keys(password)

    def enter_wrong_confirm_password(self):
        self.driver.find_element(*locators['PasswordField']).send_keys('Test1')
        self.driver.find_element(*locators['ConfirmPasswordField']).send_keys('Test')
        self.wait.until(visibility_of_element_located(locators['PasswordDoNotMatchText']))

    def click_register_button(self):
        self.driver.find_element(*locators['RegisterButton']).click()
        self.wait.until(visibility_of_element_located(locators['TextAfterRegister']))

    #Check Successful text
    def get_successful_text_for_register(self):
        return self.driver.find_element(*locators['TextAfterRegister']).text

    def get_password_do_not_match_text(self):
        return self.driver.find_element(*locators['PasswordDoNotMatchText']).text

    def click_cancel_button(self):
        self.driver.find_element(*locators['CancelButton']).click()
        self.wait.until(visibility_of_element_located(locators['LogoOfTheSite']))

    def check_url_home_page(self):
        return self.driver.current_url

    def check_title_home_page(self):
        return self.driver.title

    def get_logo_text(self):
        return self.driver.find_element(*locators['LogoOfTheSite']).text

    def get_disabled_attribute(self):
        register_button = self.driver.find_element(*locators['RegisterButton'])
        if register_button.get_attribute('disabled'):
            print('The button is not active')

    def register_user_for_login(self):
        self.driver.find_element(*locators['UsernameField']).send_keys('OksanaS')
        self.driver.find_element(*locators['FirstNameField']).send_keys('Oksana')
        self.driver.find_element(*locators['LastNameField']).send_keys('Testing')
        self.driver.find_element(*locators['PasswordField']).send_keys('Test@1234')
        self.driver.find_element(*locators['ConfirmPasswordField']).send_keys('Test@1234')
        self.driver.find_element(*locators['RegisterButton']).click()
        self.wait.until(visibility_of_element_located(locators['TextAfterRegister']))

    def get_user_already_exits_text(self):
        return self.driver.find_element(*locators['TextAfterRegister']).text




