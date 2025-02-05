import requests
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located, \
    presence_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait
from POM.page_objects.base_object import BaseObject
from selenium.webdriver.common.by import By


locators = {
    'LamborghiniTitleText': (By.CSS_SELECTOR, '.card-header'),
    'InformationAboutLamborghiniText': (By.XPATH, '//*[@class="col-md-9"]'),
#Diablo Car
    'DiabloLink': (By.XPATH, '//*[@class="cars table table-hover"]/tbody/tr[1]/td[2]/a'),
    'DiabloImageLink': (By.XPATH, '//*[@class="cars table table-hover"]/tbody/tr[1]/td[1]/a'),
    'DiabloViewMoreLink': (By.XPATH, '//*[@class="cars table table-hover"]/tbody/tr[1]/td[5]/a'),
    'DiabloTextOnDiabloPage': (By.XPATH, '/html/body/my-app/div/main/my-model/div/div[2]/h3'),
#Images
    'AllImages': (By.TAG_NAME, 'img'),
#Number of the Page
    'LeftArrowIcon': (By.XPATH, '/html/body/my-app/div/main/my-make/div/div[2]/div/my-pager/div/div/a[1]'),
    'RightArrowIcon': (By.XPATH, '/html/body/my-app/div/main/my-make/div/div[2]/div/my-pager/div/div/a[2]'),
    'NumberField': (By.XPATH, '/html/body/my-app/div/main/my-make/div/div[2]/div/my-pager/div/div/input'),
    'PageText1or2': (By.XPATH, '/html/body/my-app/div/main/my-make/div/div[2]/div/my-pager/div/div'),

}

class PopularMakePage(BaseObject):

    #Diablo Model
    def click_diablo_link(self):
        self.driver.find_element(*locators['DiabloLink']).click()
        self.wait.until(visibility_of_element_located(locators['DiabloTextOnDiabloPage']))

    def get_diablo_text_from_diablo_page(self):
        return self.driver.find_element(*locators['DiabloTextOnDiabloPage']).text

    def click_diablo_image_link(self):
        self.wait.until(element_to_be_clickable(locators['DiabloImageLink']))
        self.driver.find_element(*locators['DiabloImageLink']).click()
        self.wait.until(visibility_of_element_located(locators['DiabloTextOnDiabloPage']))

    def click_diablo_view_more_link(self):
        self.wait.until(element_to_be_clickable(locators['DiabloViewMoreLink']))
        self.driver.find_element(*locators['DiabloViewMoreLink']).click()
        self.wait.until(visibility_of_element_located(locators['DiabloTextOnDiabloPage']))

#All images on the Popular Make Page
    def check_all_images(self):
        # find all images, which are on the page (use "FIND ELEMENTS")
        self.wait.until(visibility_of_element_located(locators['AllImages']))
        images = WebDriverWait(self.driver, 10).until(presence_of_all_elements_located(locators['AllImages']))
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

    def right_arrow_icon_is_disabled(self):
        self.wait.until(element_to_be_clickable(locators['RightArrowIcon']))
        right_arrow = self.driver.find_element(*locators['RightArrowIcon'])
        return 'disabled' in right_arrow.get_attribute('class')

    def left_arrow_icon_is_disabled(self):
        self.wait.until(element_to_be_clickable(locators['LeftArrowIcon']))
        right_arrow = self.driver.find_element(*locators['LeftArrowIcon'])
        return 'disabled' in right_arrow.get_attribute('class')

    def click_right_arrow_icon(self):
        self.driver.find_element(*locators['RightArrowIcon']).click()
        self.wait.until(element_to_be_clickable(locators['LeftArrowIcon']))

    def get_number_of_current_page(self):
        self.wait.until(visibility_of_element_located(locators['NumberField']))
        return self.driver.find_element(*locators['NumberField']).get_attribute("value")

    def click_left_arrow_icon(self):
        self.wait.until(element_to_be_clickable(locators['LeftArrowIcon']))
        self.driver.find_element(*locators['LeftArrowIcon']).click()

    def get_page_text_1or2(self):
        element = self.driver.find_element(*locators['PageText1or2'])
        return element.text

