import unittest

from POM.page_objects.base_object import driver
from POM.page_objects.popular_make_page import PopularMakePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PopularMakePageTestSuits(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.popular_make_page = PopularMakePage(cls.driver, cls.wait)
        cls.driver.get('http://buggy.justtestit.org/') #Open Start Page
        cls.driver.maximize_window()
        cls.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/make/ckl2phsabijs71623vk0"]')))
        cls.driver.find_element(By.CSS_SELECTOR, 'a[href="/make/ckl2phsabijs71623vk0"]').click()
        cls.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.card-header')))

    def test_diablo_model(self):
        self.popular_make_page.click_diablo_link()
        self.assertEqual('Diablo', self.popular_make_page.get_diablo_text_from_diablo_page())
        self.driver.back()
        self.popular_make_page.click_diablo_image_link()
        self.assertEqual('Diablo', self.popular_make_page.get_diablo_text_from_diablo_page())
        self.driver.back()
        self.popular_make_page.click_diablo_view_more_link()
        self.assertEqual('Diablo', self.popular_make_page.get_diablo_text_from_diablo_page())

    def test_all_images_first_page(self):
        self.popular_make_page.check_all_images()

    def test_all_images_second_page(self):
        self.popular_make_page.click_right_arrow_icon()
        self.popular_make_page.check_all_images()

    def test_number_of_the_page(self):
        #open the second page (right arrow)
        self.popular_make_page.click_right_arrow_icon()
        self.assertEqual('2', self.popular_make_page.get_number_of_current_page())
        self.assertEqual('page 2 of 2', self.popular_make_page.get_page_text_1or2().replace('« » ',''))
        self.assertEqual(True, self.popular_make_page.right_arrow_icon_is_disabled())
        #open the first page (left arrow)
        self.popular_make_page.click_left_arrow_icon()
        self.assertEqual('1', self.popular_make_page.get_number_of_current_page())
        self.assertEqual('page 1 of 2', self.popular_make_page.get_page_text_1or2().replace('« » ',''))
        self.assertEqual(True, self.popular_make_page.left_arrow_icon_is_disabled())




        @classmethod
        def tearDownClass(cls) -> None:
            cls.driver.quit()
