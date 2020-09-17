# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re, random


class ScrawlingExceptionHandler(Exception):
    pass


class TollWebsiteAccess(object):
    toll_site_url = "https://www.ezpassnj.com/vector/violations/violationList.do"

    def __init__(self, url=toll_site_url):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.implicitly_wait(20)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
        self._pay_plan = None
        self._email = None

    def collect_login_credentials(self):
        username = input("Please enter a valid Pay Plan:")
        password = input("Please enter a valid Email:")
        self._pay_plan = username
        self._email = password
        return self._login()

    def test_site_access(self):
        host = self.base_url
        randint = random.random() * 10000
        self.driver.get("https://" + host)

    def _login(self):
        """we do the click and data entry into tables
        then login below:"""
        # We need a try except block here!
        pay_plan = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/'
                                                     'form/div/div[1]/div[3]/div[1]/div/div[1]/input').click()
        pay_plan.send_keys(self._pay_plan)
        email = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/'
                                                  'div/form/div/div[1]/div[3]/div[2]/div/div[1]/input').click()
        email.send_keys(self._email)
        login = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/'
                                                  'div/div/form/div/div[2]/div[2]/button').click()
        if login:
            return f'Success!'
        return f'Fail!'


def main():
    process = TollWebsiteAccess()
    process.test_site_access()
    process.collect_login_credentials()


if __name__ == '__main__':
    main()
