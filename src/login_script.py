#!/bin/python3
# Author: Sebastian Opiyo.
# Date Created: Sep 21, 2020
# Date Modified: Sep 21, 2020
# Description: An Amazon Toll Scraping Bot: Login page.
# -*- coding: utf-8 -*-

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time


# home url: https://www.ezpassnj.com/vector/violations/violationInquiry.do

class BotExceptionHandler(Exception):
    pass


class TollWebsiteAccess(object):
    url = "https://www.ezpassnj.com/vector/violations/violationList.do"

    def __init__(self, URL=url):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # To resolve issues with phantom--my preference.
        # self.driver = webdriver.PhantomJS(executable_path='/home/intelligentbots/Projects/web-scraper-bot/phantomjs')
        self.driver.implicitly_wait(1000)
        self.base_url = URL
        self.verificationErrors = []
        self.accept_next_alert = True
        self._pay_plan = None
        self._email = None

    def collect_login_credentials(self):
        username = input("Please enter a valid Pay Plan:")
        password = input("Please enter a valid Email:")
        self._pay_plan = username
        self._email = password

    def test_site_access(self):
        try:
            self.driver.get(self.base_url)
            print("Site can be reached!")
        except BotExceptionHandler:
            # Does this really work?
            print("Bot could not access the page...is the vpn ok?")

    def login(self):
        """We do the click and data entry into tables then login below:
        We have 3 sec pause between each input just to ensure the bot
        is not that instant, and we get to see what it actually does."""
        try:
            self.driver.get(self.base_url)
        except BotExceptionHandler:
            print("The Bot Failed to Access the site!!")

        self.collect_login_credentials()

        try:
            pay_plan = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/'
                                                         'div/form/div/div[2]/div[3]/div[1]/div/div[1]/input')
            self.driver.execute_script("arguments[0].click();", pay_plan)
            pay_plan.send_keys(self._pay_plan.strip())

            time.sleep(3)

            email = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/div/'
                                                      'div[2]/div[3]/div[2]/div/div[1]/input')
            self.driver.execute_script("arguments[0].click();", email)
            email.send_keys(str(self._email))

            time.sleep(3)

            submit_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/div/'
                                                              'div[3]/div[2]/button')
            self.driver.execute_script("arguments[0].click();", submit_button)
            submit_button.submit()

            time.sleep(120)
            print("Login Successful!!")
        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")

    def logout(self):
        try:
            sign_out = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/'
                                                         'div[3]/div/div/form/div/div[1]/div/div[3]/button')
            self.driver.execute_script("arguments[0].click();", sign_out)
        except:
            raise BotExceptionHandler("The Bot could not sign out!")

    @property
    def timer(self):
        """Does ensure that the page loads successfully before login credentials are submitted."""
        return time.sleep(7200)

    # getter and setter methods for the login credentials.
    def get_email(self):
        return self._email

    def get_payment_plan(self):
        return self._pay_plan

    def quit_browser(self):
        return self.driver.close()


def main_run():
    process = TollWebsiteAccess()
    process.test_site_access()
    print("Your credentials:")
    process.login()
    print(f'Toll Acc: {process.get_payment_plan()}')
    print(f'Acc. Mail {process.get_email()}')


if __name__ == '__main__':
    main_run()
