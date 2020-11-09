#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 09, 2020
# Date Modified: Nov 09, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet(Sunpass Account).
# -*- encoding: utf-8 -*-


"""
- Check for sight accessability (click My SunPass at the right hand corner)
- Collect logins 
- Sign in attempt, on success
- Click activity located on the left menu
- Select Filter by Toll Transaction
- Enter start and End Dates & Click View.
- Export Transaction to Spreadsheet(Download the spreadsheet)
"""


from src.login_script import TollWebsiteAccess, BotExceptionHandler
import time


class SunPassLogin(TollWebsiteAccess):

    def login_into_sun_pass(self):
        try:
            time.sleep(5)
            pay_plan = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/'
                                                         'div/form/div/div[2]/div[3]/div[1]/div/div[1]/input')
            self.driver.execute_script("arguments[0].click();", pay_plan)
            pay_plan.send_keys(self._pay_plan.strip())

            time.sleep(2)
            # ScrapeTolls.take_screen_shot(self, 'selection1.png')
            email = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/div/'
                                                      'div[2]/div[3]/div[2]/div/div[1]/input')
            self.driver.execute_script("arguments[0].click();", email)
            email.send_keys(str(self._email))
            time.sleep(2)
            # ScrapeTolls.take_screen_shot(self, 'selection2.png')
            submit_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/div/'
                                                              'div[3]/div[2]/button')
            self.driver.execute_script("arguments[0].click();", submit_button)
            time.sleep(180)
            print("Login Successful!!")
        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")