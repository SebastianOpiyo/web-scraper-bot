#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 16, 2020
# Date Modified: Nov 16, 2020
# Description: An Amazon Toll Scraping Bot: Login page (For EZ-Pass Amazon Accounts).
# -*- coding: utf-8 -*-


from src.login_script import TollWebsiteAccess, BotExceptionHandler
from selenium.webdriver.support.ui import Select
from src.toll_scraper import ScrapeTolls
import time

"""
www.ezpass.csc.paturnpike.com/PovEntryPages/Main.aspx
    • Gain access to the account 
    • Click View Transactions (under Transaction Information header on left side menu)  
    • Enter start and end dates, filter by toll transactions, and click Download Transactions to CSV
"""


class PaEzPass(TollWebsiteAccess):
    # TODO: To be done.

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
            ScrapeTolls.take_screen_shot(self, 'login_check.png')

        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")

    def logout(self):
        pass

    def scrape_tolls(self):
        # Click view transactions
        view_transactions = self.driver.find_element_by_link_text('View Transactions')
        self.driver.execute_script("arguments[0].click();", view_transactions)
        # Fill the form -- date and transaction type.
        start_date_value = input('Enter Start Date: ')
        end_date_value = input('Enter End Date: ')

        start_date = self.driver.find_element_by_name('ctl00$ContentPlaceHolder$StartDateTextBox')
        self.driver.execute_script("arguments[0].click();", start_date)
        start_date.clear()
        start_date.send_keys(start_date_value)

        end_date = self.driver.find_element_by_name('ctl00$ContentPlaceHolder$EndDateTextBox')
        self.driver.execute_script("arguments[0].click();", end_date)
        end_date.clear()
        end_date.send_keys(end_date_value)
        ScrapeTolls.take_screen_shot(self, 'datefill_check.png')

        select = Select(self.driver.find_element_by_name('ctl00$ContentPlaceHolder$FilterByDropDownList'))
        select.select_by_visible_text('Toll Transactions')
        ScrapeTolls.take_screen_shot(self, 'formfill_check.png')
        # call the download methods
        PaEzPass.download_tolls(self)

    def download_tolls(self):
        download_link = self.driver.find_element_by_id('ctl00_ContentPlaceHolder_DownloadTransactionsButton')
        self.driver.execute_script("arguments[0].click();", download_link)

