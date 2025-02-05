import unittest
from POM.page_objects.profile_page import ProfilePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProfilePageTestSuits(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.profile_page = ProfilePage(cls.driver, cls.wait)
        cls.driver.get('http://buggy.justtestit.org/') #Open Start Page
        cls.driver.find_element(By.XPATH, '//*[@class="form-group"]/input[1]').send_keys('OksanaS') #Login Field
        cls.driver.find_element(By.XPATH, '//*[@class="form-group"]/input[2]').send_keys('Test@1234') #Password Field
        cls.driver.find_element(By.XPATH, '//*[@class="form-inline"]/button').click() #Click Login Button
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/profile"]'))) #Wait Profile Link
        cls.driver.find_element(By.CSS_SELECTOR, 'a[href="/profile"]').click() #Open Profile Page
        cls.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="row btn-block"]/div/button'))) #wait Save Button


    def test_titles_of_the_field(self):
        self.assertEqual('Basic', self.profile_page.get_basic_info_text())
        self.assertEqual('Additional Info', self.profile_page.get_additional_info_text())
        self.assertEqual('Additional Info', self.profile_page.get_additional_info_password_text())
        self.assertEqual('(leave empty to keep current)', self.profile_page.get_leave_empty_to_keep_text())

    def test_basic_info_fields(self):
        self.profile_page.change_first_name()
        self.profile_page.click_save_button()
        self.assertEqual('The profile has been saved successful',
                         self.profile_page.get_successful_text_after_save())
        self.assertEqual('NewFirstName', self.profile_page.get_first_name_text())
        self.assertEqual('Hi, NewFirstName', self.profile_page.get_hi_user_text())
        self.profile_page.change_last_name()
        self.profile_page.click_save_button()
        self.assertEqual('The profile has been saved successful',
                         self.profile_page.get_successful_text_after_save())
        self.assertEqual('LastNameSyrota', self.profile_page.get_last_name_text())

    def test_enter_data_additional_fields(self):
        self.profile_page.enter_text_in_gender_field()
        self.profile_page.enter_age()
        self.profile_page.enter_address()
        self.profile_page.enter_phone()
        self.profile_page.select_hobby_from_list()
        self.profile_page.click_save_button()
        self.assertEqual('The profile has been saved successful',
                         self.profile_page.get_successful_text_after_save())
        self.assertEqual('Female', self.profile_page.get_gender_text())
        self.assertEqual('33', self.profile_page.get_age_text())
        self.assertEqual('7107 Aptos Beach, San Jose, Ca', self.profile_page.get_address_text())
        self.assertEqual('+1(669)3509772', self.profile_page.get_phone_text())
        #check list using SELECT option
        self.assertEqual(['Hiking', 'Reading', 'Working', 'Learning',
                          'Video Games', 'Biking', 'Movies', 'Reading Comics',
                          'Drawing', 'Jogging', 'Knitting', 'Bird-watching', 'Other'],
                         [item.text for item in Select(self.profile_page.get_hobby_list()).options])
        self.assertEqual('Other', self.profile_page.get_selected_hobby())

    #Additional Info (Change Password)
    def test_reset_password(self):
        self.profile_page.reset_password('Test@1234', 'Test12345@')
        self.assertEqual('The profile has been saved successful',
                         self.profile_page.get_successful_text_after_save())
                       #this function return old password (preferred method!!!!!!!!)
        self.profile_page.reset_password('Test12345@', 'Test@1234')

    #Leave Current Password field empty
    def test_current_password_field_empty(self):
        self.profile_page.enter_new_password('Test12345@')
        self.profile_page.enter_confirm_password('Test12345@')
        self.profile_page.click_save_button()
        self.assertEqual('InvalidParameter: 1 validation error(s) found. '
                         '- minimum field size of 6, ChangePasswordInput.PreviousPassword.',
                         self.profile_page.get_successful_text_after_save())

    #Enter Wrong Current Password and the same new password and confirm password
    def test_wrong_current_password(self):
        self.profile_page.enter_current_password('Test1234')
        self.profile_page.enter_new_password('Test1235')
        self.profile_page.enter_confirm_password('Test1235')
        self.profile_page.click_save_button()
        self.assertEqual('NotAuthorizedException: Incorrect username or password.',
                         self.profile_page.get_successful_text_after_save())

    #Enter part of the new password (wait until message is appeared)
    def test_part_new_password(self):
        self.profile_page.enter_new_password('Test')
        self.assertEqual('Passwords do not match', self.profile_page.get_password_do_not_match_text())

    #Click Cancel Button
    def test_cancel_button(self):
        self.profile_page.click_cancel_button()
        self.assertEqual('https://buggy.justtestit.org/', self.profile_page.check_url_home_page())
        self.assertEqual('Buggy Cars Rating', self.profile_page.check_title_home_page())
        self.assertEqual('Buggy Rating', self.profile_page.get_logo_text())


        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
