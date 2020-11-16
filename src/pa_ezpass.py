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
www.ezpass.csc.paturnpike.com/PovEntryPages/Main.aspx
    • Gain access to the account 
    • Click View Transactions (under Transaction Information header on left side menu)  
    • Enter start and end dates, filter by toll transactions, and click Download Transactions to CSV
"""


class PaEzPass(TollWebsiteAccess):

    def __init__(self):
        super().__init__()

    def login_into_pa_ezpass(self):
        try:
            user_name = self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder_UserNameTextBox"]')
            self.driver.execute_script("arguments[0].click();", user_name)
            time.sleep(1)
            user_name.send_keys(self._pay_plan.strip())
            time.sleep(1)
            pass_word = self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder_PasswordTextBox"]')
            self.driver.execute_script("arguments[0].click();", pass_word)
            pass_word.send_keys(self._email.strip())
            time.sleep(1)
            login_button = self.driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder_lbLogin"]/span')
            self.driver.execute_script("arguments[0].click();", login_button)

        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")

    def logout(self):
        pass

    def scrape_tolls(self):
        pass

    def download_tolls(self):
        pass

