import unittest
from POM.page_objects.register_page import RegisterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome


class RegisterPageTestSuits(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 60)
        cls.register_page = RegisterPage(cls.driver, cls.wait)

    #Register new user with valid information (create the random user every time)
    def test_register_new_user_for_test(self):
        self.register_page.open_register_page()
        self.register_page.enter_user_name()
        self.register_page.enter_first_name()
        self.register_page.enter_last_name()
        self.register_page.enter_password_and_confirm_password()
        self.register_page.click_register_button()
        self.assertEqual('Registration is successful', self.register_page.get_successful_text_for_register())

    #check if you get error message, when you entered wrong confirm password
    def test_password_do_not_match_message(self):
        self.register_page.open_register_page()
        self.register_page.enter_wrong_confirm_password()
        self.assertEqual('Passwords do not match', self.register_page.get_password_do_not_match_text())

    #check if click "Cancel" button returns Home Page (url, title, logo)
    def test_cancel_button(self):
        self.register_page.open_register_page()
        self.register_page.click_cancel_button()
        self.assertEqual('https://buggy.justtestit.org/', self.register_page.check_url_home_page())
        self.assertEqual('Buggy Cars Rating', self.register_page.check_title_home_page())
        self.assertEqual('Buggy Rating', self.register_page.get_logo_text())

    #Check if Register button is inactive, when missed information
    def test_register_button_inactive(self):
        self.register_page.open_register_page()
        self.register_page.get_disabled_attribute()

    #Register valid user and try register again to get message about "Exist user"
    def test_exists_user_message(self):
        self.register_page.open_register_page()
        self.register_page.register_user_for_login()
        self.assertEqual('UsernameExistsException: User already exists',
                         self.register_page.get_user_already_exits_text())



        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
