#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 09, 2020
# Date Modified: Nov 10, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet(Sunpass Account).
# -*- encoding: utf-8 -*-

from src.login_script import TollWebsiteAccess, BotExceptionHandler
import time

"""
    • Gain access to the account by clicking Log In/Register
    • Activity > Transactions
    • Enter start and end date and click View
    • Select CSV at the bottom of the page to download
"""


class EzPassLogin(TollWebsiteAccess):

    def login_into_ezpass(self):
        """The login credentials here belong to the payplan accounts."""
        try:
            time.sleep(5)
            print(f'Note: This Account Login is for the Payplans')
            pay_plan = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/'
                                                         'div/form/div/div[2]/div[3]/div[1]/div/div[1]/input')
            self.driver.execute_script("arguments[0].click();", pay_plan)
            pay_plan.send_keys(self._pay_plan.strip())

            time.sleep(1)
            # ScrapeTolls.take_screen_shot(self, 'selection1.png')
            email = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/div/'
                                                      'div[2]/div[3]/div[2]/div/div[1]/input')
            self.driver.execute_script("arguments[0].click();", email)
            email.send_keys(str(self._email))
            time.sleep(1)
            # ScrapeTolls.take_screen_shot(self, 'selection2.png')
            submit_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/div/'
                                                              'div[3]/div[2]/button')
            self.driver.execute_script("arguments[0].click();", submit_button)
            time.sleep(180)
            print("EZ Pass Login Successful!!")
        except BotExceptionHandler:
            print("Timeout exception or Wrong Credentials!")
        # Start scraping page by page in a given account.
        EzPassLogin.scrape_page_to_page(self)

    def logout(self):
        try:
            sign_out = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/'
                                                         'div[3]/div/div/form/div/div[1]/div/div[3]/button')
            self.driver.execute_script("arguments[0].click();", sign_out)
        except Exception as e:
            print(e)

    def scrape_page_to_page(self):
        from src.toll_scraper import ScrapeTolls
        from src.write_to_excel import WriteToExcel
        """Scrapes from the first page to the last
        @methods: - scrape_title_info; scrape_table_rows; move_to_next_page
        """
        try:
            ScrapeTolls.scrape_title_info(self)
            while ScrapeTolls.check_next_page(self):
                ScrapeTolls.scrape_table_rows(self)
                # consider instantiating the WriteToExcel class
                # Otherwise results to lots of garbage (class instance objs)
                WriteToExcel().write_csv_to_excel(self.get_payment_plan)
                ScrapeTolls.move_to_next_page(self)
        except Exception as e:
            raise e

