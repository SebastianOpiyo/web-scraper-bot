#!/bin/python3
# Author: Sebastian Opiyo.
# Date Created: Sep 21, 2020
# Date Modified: Oct 12, 2020
# Description: An Amazon Toll Scraping Bot: Login page.
# -*- coding: utf-8 -*-

"""This file manages login to the sites to be scraped.
It then calls the [toll_scraper] module classes.
"""

from selenium import webdriver
from chromedriver_py import binary_path
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import toll_scraper

import time


class BotExceptionHandler(Exception):
    pass


class TollWebsiteAccess(object):
    URL = "https://www.ezpassnj.com/vector/violations/violationList.do"

    def __init__(self, url=URL):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
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

    def test_site_access(self):
        # Check to see that the site is accessible or not
        # important because the site needs VPN ON to be accessible.
        try:
            self.driver.implicitly_wait(20)
            self.driver.get(self.base_url)
            print("Site can be reached!")
        except Exception as e:
            print(e)

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
            time.sleep(20)
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
            time.sleep(240)
            toll_scraper.ScrapeTolls.take_screen_shot(self, filename='login-page.png')
            print("Login Successful!!")
        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")

    def logout(self):
        try:
            sign_out = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/'
                                                         'div[3]/div/div/form/div/div[1]/div/div[3]/button')
            self.driver.execute_script("arguments[0].click();", sign_out)
        except Exception as e:
            print(e)

    # getter and setter helper methods for the login credentials.
    @property
    def get_email(self):
        return self._email

    @get_email.setter
    def get_email(self, email):
        self._email = email

    @property
    def get_payment_plan(self):
        return self._pay_plan

    @get_payment_plan.setter
    def get_payment_plan(self, new_pay_plan):
        self._pay_plan = new_pay_plan

    def call_scraper(self):
        # Initiates the scraping process.
        # toll_scraper.ScrapeTolls.scrape_title_info(self)
        # time.sleep(10)
        # toll_scraper.ScrapeTolls.check_all_boxes(self)
        # time.sleep(10)
        # toll_scraper.ScrapeTolls.take_screen_shot(self, filename='checkbox-page.png')
        # toll_scraper.ScrapeTolls.move_to_next_page(self)
        # toll_scraper.ScrapeTolls.take_screen_shot(self, filename='next-page.png')
        toll_scraper.ScrapeTolls.scrape_table_rows(self)

    def quit_browser(self):
        return self.driver.close()


def main_run():
    process = TollWebsiteAccess()
    scraper = toll_scraper.ScrapeTolls()
    process.test_site_access()
    print("Your credentials:")
    process.login()
    print(f'Toll Acc: {process.get_payment_plan}')
    print(f'Acc. Mail {process.get_email}')
    print(f':_______________________________* Scrapes *_________________________________')
    process.call_scraper()


if __name__ == '__main__':
    main_run()
