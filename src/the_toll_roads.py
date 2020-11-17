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
secure.thetollroads.com/customer/
    • Gain access to the account
    • Click Statements & Activity (located on the left side menu)
    • Click Find a Transaction, enter start and end dates, and click View Transactions
    • There isn’t a way to download transactions, therefore, you must copy and paste
"""


class TollRoads(TollWebsiteAccess):
    # TODO: To be done.

    def __init__(self):
        super().__init__()

    def login_into_toll_roads(self):
        try:
            user_name = self.driver.find_element_by_xpath('//*[@id="accountNum"]')
            self.driver.execute_script("arguments[0].click();", user_name)
            time.sleep(1)
            user_name.send_keys(self._pay_plan.strip())
            time.sleep(1)
            pass_word = self.driver.find_element_by_xpath('//*[@id="password"]')
            self.driver.execute_script("arguments[0].click();", pass_word)
            pass_word.send_keys(self._email.strip())
            time.sleep(1)
            login_button = self.driver.find_element_by_xpath('//*[@id="btn-submit"]')
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
