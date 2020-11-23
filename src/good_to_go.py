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
https://www.mygoodtogo.com/olcsc/
    • Gain access to the account
    • Select Account History (located on top menu)
    • Enter start and end date, select Toll under Transaction Type, and click Search
    • Click Download as CSV
"""


class GoodToGo(TollWebsiteAccess):
    # TODO: To be done.

    def __init__(self):
        super().__init__()

    def login_into_good_to_go(self):
        try:
            user_name = self.driver.find_element_by_xpath('//*[@id="gwt-uid-9"]')
            self.driver.execute_script("arguments[0].click();", user_name)
            time.sleep(1)
            user_name.send_keys(self._pay_plan.strip())
            time.sleep(1)
            pass_word = self.driver.find_element_by_xpath('//*[@id="gwt-uid-11"]')
            self.driver.execute_script("arguments[0].click();", pass_word)
            pass_word.send_keys(self._email.strip())
            time.sleep(1)
            login_button = self.driver.find_element_by_xpath('//*[@id="managerYourAccount"]/div[2]/'
                                                             'div/div/div/div/div/div[5]/div')
            self.driver.execute_script("arguments[0].click();", login_button)
            time.sleep(3)
            ScrapeTolls.take_screen_shot(self, 'login_check.png')
        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")

    def logout(self):
        pass

    def scrape_tolls(self):
        # Select Account history (located at the top)
        account_history = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/div'
                                                            '/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]')
        self.driver.execute_script("arguments[0].click();", account_history)
        # transaction_button = self.driver.find_element_by_xpath('//*[@id="myAccountHeader"]/div/div[2]'
        #                                                        '/div/div/div/div/div/div[2]/div/div/div[2]/div')
        # Enter start & end date
        start_date_value = input('Enter Start Date: ')
        end_date_value = input('Enter End Date: ')
        start_date = self.driver.find_elements_by_class_name('v-textfield v-datefield-textfield')
        end_date = self.driver.find_element_by_xpath('')
        self.driver.execute_script("arguments[0].click();", start_date)
        start_date.clear()
        start_date.send_keys(start_date_value)
        self.driver.execute_script("arguments[0].click();", end_date)
        end_date.clear()
        end_date.send_keys(end_date_value)

        # Select toll under transaction type, click search
        select = Select(self.driver.find_element_by_id('gwt-uid-102'))
        select.select_by_visible_text('Toll')
        # Download CSV
        GoodToGo.download_tolls(self)

    def download_tolls(self):
        download_link = self.driver.find_element_by_link_text('(download as CSV)')
        self.driver.execute_script("arguments[0].click();", download_link)
