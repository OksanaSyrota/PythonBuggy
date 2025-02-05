import requests
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located

from POM.page_objects.base_object import BaseObject
from selenium.webdriver.common.by import By


locators = {
#Start Page
    'PopularMake': (By.CSS_SELECTOR, 'a[href="/make/ckl2phsabijs71623vk0"]'),
    'PopularMode': (By.CSS_SELECTOR, 'a[href="/model/ckl2phsabijs71623vk0|ckl2phsabijs71623vqg"]'),
    'OverallRating': (By.CSS_SELECTOR, 'a[href="/overall"]'),
    'AllImages': (By.TAG_NAME, 'img'),
#Footer
    'FacebookIcon': (By.CSS_SELECTOR, 'a[href="https://www.facebook.com"]'),
    'FacebookText': (By.CSS_SELECTOR, '._8eso'),
    'TwitterIcon': (By.CSS_SELECTOR, 'a[href="https://www.twitter.com"]'),
    'TwitterText': (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[1]/span'),
#Popular Make Page
    'LamborghiniHeaderText': (By.CSS_SELECTOR, '.card-header'),
#Popular Mode Page
    'LamborghiniText': (By.XPATH, '//*[@class="container"]/div/div/div/h4'),
#Overall Rating Page
    'CommentsText': (By.CSS_SELECTOR, '.comments')



}

class StartPage(BaseObject):

    #Click on the all cards and check, if correct pages are displayed, return print text
    def check_main_cards(self):
        self.driver.get('http://buggy.justtestit.org/')
        self.wait.until(element_to_be_clickable(locators['PopularMake']))
        self.driver.find_element(*locators['PopularMake']).click()
        self.wait.until(visibility_of_element_located(locators['LamborghiniHeaderText']))
        print(self.driver.find_element(*locators['LamborghiniHeaderText']).text)
        self.driver.back()
        self.wait.until(element_to_be_clickable(locators['PopularMode']))
        self.driver.find_element(*locators['PopularMode']).click()
        self.wait.until(visibility_of_element_located(locators['LamborghiniText']))
        print(self.driver.find_element(*locators['LamborghiniText']).text)
        self.driver.back()
        self.wait.until(element_to_be_clickable(locators['OverallRating']))
        self.driver.find_element(*locators['OverallRating']).click()
        self.wait.until(visibility_of_element_located(locators['CommentsText']))
        print(self.driver.find_element(*locators['CommentsText']).text)
        self.driver.back()


    #All images on the start page
    def check_all_images(self):
        # find all images, which are on the page (use "FIND ELEMENTS")
        images = self.driver.find_elements(*locators['AllImages'])
        results = []
        for image in images:
            # Get the 'src' attribute
            src = image.get_attribute('src')
            if src:  # Check if 'src' is not None or empty
                try:
                    response = requests.get(src, timeout=5)
                    if response.status_code == 200:
                        results.append({"href": src, "status": "Valid"})
                    else:
                        print(f"Broken image: {src} (status code: {response.status_code})")
                except requests.exceptions.RequestException as e:
                    print(f"Error for {src}: {e}")
            else:
                print("Image with no 'src' attribute or empty 'src' attribute found.")
        print("Final results:", results)

    def facebook_link_footer(self):
        self.driver.find_element(*locators['FacebookIcon']).click()
        #switch to new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(visibility_of_element_located(locators['FacebookText']))
        actual_text = self.driver.find_element(*locators['FacebookText']).text
        expected_result = 'Connect with friends and the world around you on Facebook.'
        print(f'Expected text: {expected_result}, actual results: {actual_text}')
        #close the new tab
        self.driver.close()
        #switch back to the original tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        return expected_result, actual_text

    def twitter_link_footer(self):
        self.driver.find_element(*locators['TwitterIcon']).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(visibility_of_element_located(locators['TwitterText']))
        actual_text = self.driver.find_element(*locators['TwitterText']).text
        expected_result = 'Happening now'
        print(f'Expected text: {expected_result}, actual results: {actual_text}')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return expected_result, actual_text