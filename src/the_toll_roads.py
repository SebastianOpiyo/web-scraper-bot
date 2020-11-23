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
        # Click statements & Activity
        statement_button = self.driver.find_element_by_link_text('Statements & Activity')
        self.driver.execute_script("arguments[0].click();", statement_button)
        # Click find a Transaction
        find_transaction = self.driver.find_element_by_link_text('Find a Transaction')
        self.driver.execute_script("arguments[0].click();", find_transaction)
        # Enter start & end dates & click view transactions
        start_date_value = input('Enter Start Date: ')
        end_date_value = input('Enter End Date: ')
        start_date = self.driver.find_elements_by_id('start-date')
        end_date = self.driver.find_element_by_id('end-date')
        self.driver.execute_script("arguments[0].click();", start_date)
        start_date.clear()
        start_date.send_keys(start_date_value)
        self.driver.execute_script("arguments[0].click();", end_date)
        end_date.clear()
        end_date.send_keys(end_date_value)
        view_transaction = self.driver.find_element_by_id('btn-view')
        self.driver.execute_script("arguments[0].click();", view_transaction)

    def download_tolls(self):
        pass
