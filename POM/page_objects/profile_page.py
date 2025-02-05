from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located
from POM.page_objects.base_object import BaseObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


locators = {
#Login Form
    'LogoOfTheSite': (By.CSS_SELECTOR, '.navbar-brand'),
    'ProfileLinkNavBar': (By.CSS_SELECTOR, 'a[href="/profile"]'),
    'HiUserText': (By.XPATH, '//*[@class="nav-item"]/span'),
#Profile Page
    'BasicTitleText': (By.XPATH, '//*[@class="container my-form"]/form/div[1]/div[1]/div/h3'),
    'AdditionalInfoTitleText': (By.XPATH, '//*[@class="container my-form"]/form/div[1]/div[2]/div/h3'),
    'AdditionalInfoPasswordTitleText': (By.XPATH, '//*[@class="container my-form"]/form/div[1]/div[3]/div/h3'),
    'SaveButton': (By.XPATH, '//*[@class="row btn-block"]/div/button'),
    'SavedSuccessfulText': (By.XPATH, '//*[@class="col-lg-4"]/div[2]'),
    'CancelButtonProfilePage': (By.XPATH, '//*[@class="row btn-block"]/div/a'),
    #Basic Info
    'LoginFieldBasicInfo': (By.CSS_SELECTOR, '#username'),
    'FirstNameFieldBasicInfo': (By.CSS_SELECTOR, '#firstName'),
    'LastNameFieldBasicInfo': (By.CSS_SELECTOR, '#lastName'),
    #Additional Info
    'GenderField': (By.CSS_SELECTOR, '#gender'),
    'GenderDropDownList': (By.CSS_SELECTOR, '#genders'),
    'AgeField': (By.CSS_SELECTOR, '#age'),
    'AddressField': (By.CSS_SELECTOR, '#address'),
    'PhoneField': (By.CSS_SELECTOR, '#phone'),
    'HobbyField': (By.CSS_SELECTOR, '#hobby'),
    #Additional Info (Change Password)
    'ChangePasswordTitle': (By.XPATH, '//*[@class="container my-form"]/form/div/div[3]/div/div/div/div/h4'),
    'LeaveEmptyToKeepCurrentText': (By.XPATH, '//*[@class="container my-form"]/form/div/div[3]/div/div/div/div/h6'),
    'CurrentPasswordField': (By.CSS_SELECTOR, '#currentPassword'),
    'NewPasswordField': (By.CSS_SELECTOR, '#newPassword'),
    'ConfirmPasswordField': (By.CSS_SELECTOR, '#newPasswordConfirmation'),
    'PasswordDoNotMatchText': (By.XPATH,
                               '//*[@class="container my-form"]/form/div/div[3]/div/div/div/div[2]/fieldset[3]/div'),
    'LanguageField': (By.CSS_SELECTOR, '#language')
}

class ProfilePage(BaseObject):

    def get_hi_user_text(self):
        return self.driver.find_element(*locators['HiUserText']).text

    def get_basic_info_text(self):
        return self.driver.find_element(*locators['BasicTitleText']).text

    def get_additional_info_text(self):
        return self.driver.find_element(*locators['AdditionalInfoTitleText']).text

    def get_additional_info_password_text(self):
        return self.driver.find_element(*locators['AdditionalInfoPasswordTitleText']).text

    def get_leave_empty_to_keep_text(self):
        return self.driver.find_element(*locators['LeaveEmptyToKeepCurrentText']).text

    def change_first_name(self):
        self.wait.until(visibility_of_element_located(locators['FirstNameFieldBasicInfo']))
        self.driver.find_element(*locators['FirstNameFieldBasicInfo']).clear() #remove old information
        self.driver.find_element(*locators['FirstNameFieldBasicInfo']).send_keys('NewFirstName')

    def change_last_name(self):
        self.wait.until(visibility_of_element_located(locators['LastNameFieldBasicInfo']))
        self.driver.find_element(*locators['LastNameFieldBasicInfo']).clear() #remove old information
        self.driver.find_element(*locators['LastNameFieldBasicInfo']).send_keys('LastNameSyrota')

    def click_save_button(self):
        self.driver.find_element(*locators['SaveButton']).click()
        self.wait.until(visibility_of_element_located(locators['SavedSuccessfulText']))

    def get_successful_text_after_save(self):
        return self.driver.find_element(*locators['SavedSuccessfulText']).text

    def get_first_name_text(self):
        return self.driver.find_element(*locators['FirstNameFieldBasicInfo']).get_attribute("value")

    def get_last_name_text(self):
        return self.driver.find_element(*locators['LastNameFieldBasicInfo']).get_attribute("value")

    #Additional Info Fields
    def enter_text_in_gender_field(self):
        self.driver.find_element(*locators['GenderField']).clear()
        self.driver.find_element(*locators['GenderField']).send_keys('Female')

    def enter_age(self):
        self.driver.find_element(*locators['AgeField']).clear()
        self.driver.find_element(*locators['AgeField']).send_keys('33')

    def enter_address(self):
        self.driver.find_element(*locators['AddressField']).clear()
        (self.driver.find_element(*locators['AddressField']).
         send_keys('7107 Aptos Beach, San Jose, Ca'))

    def enter_phone(self):
        self.driver.find_element(*locators['PhoneField']).clear()
        self.driver.find_element(*locators['PhoneField']).send_keys('+1 (669) 350 9772')

    def get_gender_text(self):
        self.wait.until(visibility_of_element_located(locators['GenderField']))
        return self.driver.find_element(*locators['GenderField']).get_attribute("value")

    def get_age_text(self):
        self.wait.until(visibility_of_element_located(locators['AgeField']))
        return self.driver.find_element(*locators['AgeField']).get_attribute('value')

    def get_address_text(self):
        self.wait.until(visibility_of_element_located(locators['AddressField']))
        return self.driver.find_element(*locators['AddressField']).get_attribute('value')

    def get_phone_text(self):
        self.wait.until(visibility_of_element_located(locators['PhoneField']))
        return self.driver.find_element(*locators['PhoneField']).get_attribute('value')

    def get_hobby_list(self):
        return self.driver.find_element(*locators['HobbyField'])

    def select_hobby_from_list(self):
        Select(self.driver.find_element(*locators['HobbyField'])).select_by_visible_text('Other')

    def get_selected_hobby(self):
        return self.driver.find_element(*locators['HobbyField']).get_attribute("value")

    #Change password and reset to old password
    def reset_password(self, old_password, new_password):
        self.driver.find_element(*locators['CurrentPasswordField']).send_keys(old_password)
        self.driver.find_element(*locators['NewPasswordField']).send_keys(new_password)
        self.driver.find_element(*locators['ConfirmPasswordField']).send_keys(new_password)
        self.driver.find_element(*locators['SaveButton']).click()
        self.wait.until(visibility_of_element_located(locators['SavedSuccessfulText']))

    def enter_new_password(self, new_password):
        self.driver.find_element(*locators['NewPasswordField']).send_keys(new_password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*locators['ConfirmPasswordField']).send_keys(confirm_password)

    def enter_current_password(self, current_password):
        self.driver.find_element(*locators['CurrentPasswordField']).send_keys(current_password)

    def get_password_do_not_match_text(self):
        self.wait.until(visibility_of_element_located(locators['PasswordDoNotMatchText']))
        return self.driver.find_element(*locators['PasswordDoNotMatchText']).text

    def click_cancel_button(self):
        self.driver.find_element(*locators['CancelButtonProfilePage']).click()
        self.wait.until(element_to_be_clickable(locators['LogoOfTheSite']))

    def check_url_home_page(self):
        return self.driver.current_url

    def check_title_home_page(self):
        return self.driver.title

    def get_logo_text(self):
        return self.driver.find_element(*locators['LogoOfTheSite']).text



