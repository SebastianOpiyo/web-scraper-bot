#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 09, 2020
# Date Modified: Nov 10, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet(Sunpass Account).
# -*- encoding: utf-8 -*-

from src.login_script import TollWebsiteAccess, BotExceptionHandler
from selenium.webdriver.support.ui import Select
import time


"""
    • Gain access to the account by using "Manage My Acc on the left."
    • Click on Acc History
    • Enter start and end date
    • Select transaction type to Toll
    • Select Download in Excel
"""


class NttaLoginAndSraping(TollWebsiteAccess):
    """Ntta website login and toll scraping."""

    def __init__(self):
        super().__init__()

    def ntta_login(self):
        time.sleep(5)
        user_id = self._pay_plan.strip()
        password_id = self._email.strip()
        form_user_id = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[1]'
                                                         '/div[4]/form/div/div/input[1]')
        form_user_id.send_keys(user_id)
        form_passd = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[1]'
                                                       '/div[4]/form/div/div/input[2]')
        form_passd.send_keys(password_id)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginButton"]').click()

    def scrapping(self):
        """Fill the necessary forms and download the tolls, within a given date range. """

        from src.toll_scraper import ScrapeTolls
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/ul/li[2]/a/span').click()
        time.sleep(2)
        start_date = self.driver.find_element_by_name('startDate')
        end_date = self.driver.find_element_by_name('endDate')

        input_start_date = ScrapeTolls.start_at_given_date()
        input_end_date = ScrapeTolls.stop_at_given_date()

        start_date.clear()
        end_date.clear()
        start_date.send_keys(input_start_date)
        end_date.send_keys(input_end_date)

        select = Select(self.driver.find_element_by_name('transactionType'))
        select.select_by_visible_text('Toll')
        self.driver.find_element_by_id('displayButton').click()
        NttaLoginAndSraping.download_excel(self)

    def download_excel(self):
        download_tolls_link = self.driver.find_element_by_xpath('//*[@id="data"]/div[1]/a[2]')
        for i in range(4):
            self.driver.execute_script("arguments[0].click();", download_tolls_link)
