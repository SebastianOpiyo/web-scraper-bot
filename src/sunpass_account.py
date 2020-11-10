#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 09, 2020
# Date Modified: Nov 10, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet(Sunpass Account).
# -*- encoding: utf-8 -*-


from src.login_script import TollWebsiteAccess, BotExceptionHandler
from src.toll_scraper import ScrapeTolls
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

    def login_into_sun_pass(self):
        try:
            ScrapeTolls.take_screen_shot(self, 'site_check.png')
            time.sleep(2)
            my_sunpass_button = self.driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul/li[8]/a/span')
            self.driver.execute_script("arguments[0].click();", my_sunpass_button)
            time.sleep(2)
            ScrapeTolls.take_screen_shot(self, 'login_form_check.png')
            username = self.driver.find_element_by_xpath('//*[@id="tt_username"]')
            self.driver.execute_script("arguments[0].click();", username)
            username.send_keys(self._pay_plan.strip())
            time.sleep(1)
            site_password = self.driver.find_element_by_xpath('//*[@id="tt_loginPassword"]')
            self.driver.execute_script("arguments[0].click();", site_password)
            site_password.send_keys(str(self._email))
            time.sleep(2)
            ScrapeTolls.take_screen_shot(self, 'login_check.png')
            login_button = self.driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul/li[8]/div/form/button')
            self.driver.execute_script("arguments[0].click();", login_button)
            time.sleep(10)
            print("SunPass Login Successful!!")
            ScrapeTolls.take_screen_shot(self, 'success_login_check.png')
        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")

    def logout(self):
        pass

    def scrape_tolls(self):
        """
        - Click the activity button
        - Set the dates
        - Download the excel file.
        :return:
        """

        activity_button = self.driver.find_element_by_xpath('//*[@id="acctmenu"]/div/ul/li[8]/a')
        self.driver.execute_script("arguments[0].click();", activity_button)
        time.sleep(3)
        filter_by = self.driver.find_element_by_xpath('//*[@id="38"]/option[9]')
        self.driver.execute_script("arguments[0].click();", filter_by)
        time.sleep(1)
        ScrapeTolls.take_screen_shot(self, 'toll_selection_check.png')

    def download_tolls(self):
        """Find the download link and download the tolls excel doc."""
        pass
