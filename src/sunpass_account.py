#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 09, 2020
# Date Modified: Nov 10, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet(Sunpass Account).
# -*- encoding: utf-8 -*-


from src.login_script import TollWebsiteAccess, BotExceptionHandler
from src.toll_scraper import ScrapeTolls
from selenium.webdriver.support.ui import Select
import time


"""
- Check for sight accessibility (click My SunPass at the right hand corner)
- Collect logins 
- Sign in attempt, on success
- Click activity located on the left menu
- Select Filter by Toll Transaction
- Enter start and End Dates & Click View.
- Export Transaction to Spreadsheet(Download the spreadsheet)
"""


class SunPassLogin(TollWebsiteAccess):

    def __init__(self):
        super().__init__()

    def login_into_sun_pass(self):
        try:
            # ScrapeTolls.take_screen_shot(self, 'site_check.png')
            time.sleep(2)
            my_sunpass_button = self.driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul/li[8]/a/span')
            self.driver.execute_script("arguments[0].click();", my_sunpass_button)
            time.sleep(2)
            # ScrapeTolls.take_screen_shot(self, 'login_form_check.png')
            username = self.driver.find_element_by_xpath('//*[@id="tt_username"]')
            self.driver.execute_script("arguments[0].click();", username)
            username.send_keys(self._pay_plan.strip())
            time.sleep(1)
            site_password = self.driver.find_element_by_xpath('//*[@id="tt_loginPassword"]')
            self.driver.execute_script("arguments[0].click();", site_password)
            site_password.send_keys(str(self._email))
            time.sleep(2)
            # ScrapeTolls.take_screen_shot(self, 'login_check.png')
            login_button = self.driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul/li[8]/div/form/button')
            self.driver.execute_script("arguments[0].click();", login_button)
            time.sleep(10)
            print("SunPass Login Successful!!")
            # ScrapeTolls.take_screen_shot(self, 'success_login_check.png')
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
        from src.toll_scraper import ScrapeTolls
        # 1. Perform Filter By Selection
        activity_button = self.driver.find_element_by_xpath('//*[@id="acctmenu"]/div/ul/li[8]/a')
        self.driver.execute_script("arguments[0].click();", activity_button)
        time.sleep(3)
        # ScrapeTolls.take_screen_shot(self, 'selection_check.png')
        page_body = self.driver.find_element_by_id('searchForm')
        select = Select(page_body.find_element_by_name('filterBy'))
        select.select_by_visible_text('Toll Transaction')
        time.sleep(1)
        # ScrapeTolls.take_screen_shot(self, 'toll_selection_check.png')
        # 1. Enter Start Date & End Date.
        start_date_value = ScrapeTolls.start_at_given_date()
        end_date_value = ScrapeTolls.stop_at_given_date()
        # We clear and enter values.
        start_date_input = page_body.find_element_by_name('startDateAll')
        start_date_input.clear()
        self.driver.execute_script("arguments[0].click();", start_date_input)
        start_date_input.send_keys(start_date_value)
        end_date_input = page_body.find_element_by_name('endDateAll')
        end_date_input.clear()
        self.driver.execute_script("arguments[0].click();", end_date_input)
        end_date_input.send_keys(end_date_value)
        ScrapeTolls.take_screen_shot(self, 'date_values_check.png')

        # Call the download function after everything is set.
        SunPassLogin.download_tolls(self)

    def download_tolls(self):
        """Find the download link and download the tolls excel doc."""

        download_csv = self.driver.find_element_by_xpath('//*[@id="winphexcel"]')
        self.driver.execute_script("arguments[0].click();", download_csv)
        # ScrapeTolls.take_screen_shot(self, 'download_csv_check.png')
