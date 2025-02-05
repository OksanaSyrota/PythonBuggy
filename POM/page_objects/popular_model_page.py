import time

import requests
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located, \
    presence_of_all_elements_located, text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait
from POM.page_objects.base_object import BaseObject
from selenium.webdriver.common.by import By


locators = {
    'DiabloText': (By.XPATH, '/html/body/my-app/div/main/my-model/div/div[2]/h3'),
    'LamborghiniText': (By.XPATH, '/html/body/my-app/div/main/my-model/div/div[1]/div[1]/div[2]/h4'),
    'SpecificationText': (By.XPATH, '/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[1]/div/h4'),
    'EngineText': (By.XPATH, '/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[1]/div/ul/li[1]'),
    'MaxSpeedText': (By.XPATH, '/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[1]/div/ul/li[2]'),
    'VotesText': (By.XPATH, '/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div/h4'),
    'NumberOfVotes': (By.XPATH, '/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div/h4/strong'),
    'YouNeedToBeLoggedToVoteText': (By.XPATH, '/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[2]/p'),
    'LoginField': (By.CSS_SELECTOR, '[name="login"]'),
    'PasswordField': (By.CSS_SELECTOR, '[name="password"]'),
    'LoginButton': (By.XPATH, '//*[@class="form-inline"]/button'),
    'Vote!Button': (By.CSS_SELECTOR, '.btn-block'),
    'CommentField': (By.CSS_SELECTOR, '#comment'),
    'YourCommentText': (By.CSS_SELECTOR, '[for="comment"]'),
    'LogoutButton': (By.CSS_SELECTOR, 'a[href="javascript:void(0)"]'),
    'ThankYouForYourVoteText': (By.XPATH, 'html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[2]/p'),
}

class PopularModelPage(BaseObject):


    def get_lamborghini_text(self):
        return self.driver.find_element(*locators['LamborghiniText']).text

    def get_diablo_text(self):
        return self.driver.find_element(*locators['DiabloText']).text

    def get_specification_text(self):
        return self.driver.find_element(*locators['SpecificationText']).text

    def get_engine_text(self):
        return self.driver.find_element(*locators['EngineText']).text

    def get_max_speed_text(self):
        return self.driver.find_element(*locators['MaxSpeedText']).text

    def get_votes_text(self):
        return self.driver.find_element(*locators['VotesText']).text

    def get_number_of_votes_text(self):
        self.wait.until(visibility_of_element_located(locators['NumberOfVotes']))
        return self.driver.find_element(*locators['NumberOfVotes']).text.strip()

    def get_you_need_to_be_logged_text(self):
        self.wait.until(visibility_of_element_located(locators['YouNeedToBeLoggedToVoteText']))
        return self.driver.find_element(*locators['YouNeedToBeLoggedToVoteText']).text

    def login_to_account(self):
        self.driver.find_element(*locators['LoginField']).send_keys('Test8')
        self.driver.find_element(*locators['PasswordField']).send_keys('Test@1234')
        self.wait.until(element_to_be_clickable(locators['LoginButton']))
        self.driver.find_element(*locators['LoginButton']).click()

    def click_vote_button(self):
        self.wait.until(element_to_be_clickable(locators['Vote!Button']))
        self.driver.find_element(*locators['Vote!Button']).click()

    def get_thank_you_for_vote_text(self):
        self.wait.until(text_to_be_present_in_element(
            locators['ThankYouForYourVoteText'], 'Thank you for your vote!'
        ))
        return self.driver.find_element(*locators['ThankYouForYourVoteText']).text

    def get_your_comment_text(self):
        self.wait.until(visibility_of_element_located(locators['YourCommentText']))
        return self.driver.find_element(*locators['YourCommentText']).text

    def logout_from_account(self):
        self.wait.until(element_to_be_clickable(locators['LogoutButton']))
        self.driver.find_element(*locators['LogoutButton']).click()
        time.sleep(3)
        self.driver.delete_all_cookies()

