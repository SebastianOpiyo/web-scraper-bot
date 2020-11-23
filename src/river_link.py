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
            RiverLink.scrape_tolls(self)
            ScrapeTolls.take_screen_shot(self, 'download_check.png')

        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")

    def logout(self):
        pass

    def scrape_tolls(self):
        # Move to acc features > transaction history
        caret_click = self.driver.find_element_by_link_text('ACCOUNT FEATURES')
        self.driver.execute_script("arguments[0].click();", caret_click)
        ScrapeTolls.take_screen_shot(self, 'features_check.png')
        # click set filters, select toll as transaction type
        time.sleep(3)
        transactions_link = self.driver.find_element_by_link_text('Transaction History')
        self.driver.execute_script("arguments[0].click();", transactions_link)
        ScrapeTolls.take_screen_shot(self, 'transactions_check.png')
        time.sleep(2)
        # set date & click Apply
        set_filters = self.driver.find_element_by_id('btnSetFilters')
        self.driver.execute_script("arguments[0].click();", set_filters)
        ScrapeTolls.take_screen_shot(self, 'filters_check.png')
        # Select toll
        select = Select(self.driver.find_element_by_name('ctl00$MainContent$ddlFilterType'))
        select.select_by_visible_text('Toll')
        ScrapeTolls.take_screen_shot(self, 'selectToll_check.png')
        # Enter Date.
        set_date = input('From Date: ')
        date_input = self.driver.find_element_by_name('ctl00$MainContent$txtFilterDate')
        self.driver.execute_script("arguments[0].click();", date_input)
        date_input.send_keys(set_date)
        click_apply = self.driver.find_element_by_name('ctl00$MainContent$btnApplyFilter')
        self.driver.execute_script("arguments[0].click();", click_apply)
        # call download function.
        RiverLink.download_tolls(self)
        time.sleep(3)
        ScrapeTolls.take_screen_shot(self, 'downloadpg_check.png')

    def download_tolls(self):
        download_button = self.driver.find_element_by_name('ctl00$MainContent$databound2$btnDownloadCSV')
        self.driver.execute_script("arguments[0].click();", download_button)

