import unittest
from POM.page_objects.start_page import StartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome


class StartPageTestSuits(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 60)
        cls.start_page = StartPage(cls.driver, cls.wait)

    def test_start_page(self):
        self.start_page.check_main_cards()
        self.start_page.check_all_images()
        self.start_page.facebook_link_footer()
        self.start_page.twitter_link_footer()


        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
