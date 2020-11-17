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
https://riverlink.com/RiverLink.External/Account/AccountSummary.aspx
    • Gain access to the account
    • Account Features > Transaction History
    • Click Set Filters, select Toll as Transaction Type, enter in date, and click Apply
    • Click Download CSV
"""


class RiverLink(TollWebsiteAccess):
    # TODO: To be done.
    def __init__(self):
        super().__init__()

    def login_into_river_link(self):
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
            ScrapeTolls.take_screen_shot(self, 'login_check.png')

        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")

    def logout(self):
        pass

    def scrape_tolls(self):
        pass

    def download_tolls(self):
        pass

