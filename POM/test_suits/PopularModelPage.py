import unittest

from POM.page_objects.base_object import driver
from POM.page_objects.popular_model_page import PopularModelPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PopularModelPageTestSuits(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.popular_model_page = PopularModelPage(cls.driver, cls.wait)
        cls.driver.get('http://buggy.justtestit.org/') #Open Start Page
        cls.driver.maximize_window()
        cls.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                   'a[href="/model/ckl2phsabijs71623vk0|ckl2phsabijs71623vqg"]')))
        cls.driver.find_element(By.CSS_SELECTOR,
                                'a[href="/model/ckl2phsabijs71623vk0|ckl2phsabijs71623vqg"]').click()
        cls.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         '/html/body/my-app/div/main/my-model/div/div[2]/h3')))

    def test_popular_model_text(self):
        self.assertEqual('Lamborghini', self.popular_model_page.get_lamborghini_text())
        self.assertEqual('Diablo', self.popular_model_page.get_diablo_text())
        self.assertEqual('Engine: 6.0l', self.popular_model_page.get_engine_text())
        self.assertEqual('Max Speed: 25km/h', self.popular_model_page.get_max_speed_text())
        self.assertEqual('Votes: 3563', self.popular_model_page.get_votes_text())
        self.assertEqual('3563', self.popular_model_page.get_number_of_votes_text())
        self.assertEqual('You need to be logged in to vote.',
                         self.popular_model_page.get_you_need_to_be_logged_text())

    def test_votes_after_login(self):
        self.popular_model_page.login_to_account()
        self.assertEqual('Your Comment (optional)', self.popular_model_page.get_your_comment_text())
        self.popular_model_page.click_vote_button()
        #self.assertEqual('Thank you for your vote!', self.popular_model_page.get_thank_you_for_vote_text())
        self.popular_model_page.logout_from_account()
        self.assertEqual('You need to be logged in to vote.',
                         self.popular_model_page.get_you_need_to_be_logged_text())
#just check GitHub!!!!


        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
