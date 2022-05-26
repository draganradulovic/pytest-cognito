from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.support.select import Select

#Class Selenium_actions contains basic selenium commands
class Selenium_actions():
    def __init__(self,driver):
        self.driver = driver

    def findBy(self, by):
        by=by.lower()
        if by=='xpath':
            return By.XPATH
        if by=='id':
            return By.ID
        if by=='class':
            return By.CLASS_NAME
        if by=='tag_name':
            return By.TAG_NAME

    def get_element(self,element,by='xpath'):
        el=self.driver.find_element(self.findBy(by) ,element)
        return el

    def click_element(self, element, by='xpath'):
        self.get_element(element, by).click()

    def send_keys(self,keys, element, by='xpath'):
        self.scroll_by_elem(element, by)
        self.get_element(element, by).send_keys(keys)

    def scroll_by_elem(self, element, by='xpath'):
        try:
            element=self.get_element(element, by)
            location = element.location_once_scrolled_into_view
            self.driver.execute_script("window.scrollBy(0, -160);")
        except:
            print("Can not scroll")



