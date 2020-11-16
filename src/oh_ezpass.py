#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 16, 2020
# Date Modified: Nov 16, 2020
# Description: An Amazon Toll Scraping Bot: Login page (For EZ-Pass Amazon Accounts).
# -*- coding: utf-8 -*-


from src.login_script import TollWebsiteAccess, BotExceptionHandler
from src.toll_scraper import ScrapeTolls
import time

"""
https://www.ezpassoh.com/EntryPages/Login.aspx
    • Gain access to the account
    • Click Transactions (located on top menu)
    • Select Custom dates, enter start and end dates, and click Retrieve Transactions
    • There isn’t a way to download transactions, therefore, you must copy and paste
"""


class OhEzPass(TollWebsiteAccess):

    def __init__(self):
        super().__init__()

    def login_into_ohio_ezpass(self):
        try:
            user_name = self.driver.find_element_by_xpath('//*[@id="txtUserName"]')
            self.driver.execute_script("arguments[0].click();", user_name)
            time.sleep(1)
            user_name.send_keys(self._pay_plan.strip())
            time.sleep(1)
            pass_word = self.driver.find_element_by_xpath('//*[@id="txtPassword"]')
            self.driver.execute_script("arguments[0].click();", pass_word)
            pass_word.send_keys(self._email.strip())
            time.sleep(1)
            login_button = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
            self.driver.execute_script("arguments[0].click();", login_button)

        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")

    def logout(self):
        pass

    def scrape_tolls(self):
        pass

    def download_tolls(self):
        pass
