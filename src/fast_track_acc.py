#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 16, 2020
# Date Modified: Nov 16, 2020
# Description: An Amazon Toll Scraping Bot: Login page (For EZ-Pass Amazon Accounts).
# -*- coding: utf-8 -*-


from src.login_script import TollWebsiteAccess, BotExceptionHandler
from src.toll_scraper import ScrapeTolls
from selenium.webdriver.support.ui import Select
import time

"""
site url = https://www.bayareafastrak.org/vector/account/home/accountLogin.do
    • Gain access to the account
    • Click Transactions (located on the left side menu)
    • Enter start and end dates and click View
    • Select CSV at the bottom of the page to download
"""


class FastTrack(TollWebsiteAccess):
    # TODO: To be done.

    def __init__(self):
        super().__init__()

    def login_into_fast_track(self):
        try:
            user_name = self.driver.find_element_by_id('tt_username1')
            self.driver.execute_script("arguments[0].click();", user_name)
            time.sleep(2)
            user_name.send_keys(self._pay_plan.strip())
            time.sleep(1)
            pass_word = self.driver.find_element_by_xpath('//*[@id="tt_loginPassword1"]')
            self.driver.execute_script("arguments[0].click();", pass_word)
            pass_word.send_keys(str(self._email))
            time.sleep(1)
            login_button = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/form/button')
            self.driver.execute_script("arguments[0].click();", login_button)
            ScrapeTolls.take_screen_shot(self, 'login_check.png')

        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")

    def logout(self):
        pass

    def scrape_tolls(self):
        """
        - Click the activity button
        - Set the dates
        - Download the excel file.
        :methods: download_tolls - called after form has been filled accordingly.
        :return: csv file.
        """
        # 1. Click Transactions (located on the left side menu)
        tranxn_link = self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]/a')
        self.driver.execute_script("arguments[0].click();", tranxn_link)
        # 2. Enter start and end dates and click View
        # from_date = input('')
        # to_date = input('')
        # The values for the below variables can be split from one of the input above.
        # target_year = ''
        # target_month = ''
        # target_day = ''

        # 3. Download CSV
        download_csv = self.driver.find_element_by_link_text('CSV')
        self.driver.execute_script("arguments[0].click();", download_csv)

        # Call the download function after everything is set.
        FastTrack.download_tolls(self)

    def download_tolls(self):
        """Find the download link and download the tolls excel doc."""

        download_csv = self.driver.find_element_by_link_text('CSV')
        self.driver.execute_script("arguments[0].click();", download_csv)
