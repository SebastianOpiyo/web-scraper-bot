#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Sep 21, 2020
# Date Modified: Oct 28, 2020
# Description: An Amazon Toll Scraping Bot: Login page (For EZ-Pass Amazon Accounts).
# -*- coding: utf-8 -*-

"""This file manages login to the sites to be scraped.
It then calls the [toll_scraper] module classes.
"""

from src.base import BasePage
import time


class BotExceptionHandler(Exception):
    """A common base class for other Bot Exception Error handling classes.."""
    pass


class TollWebsiteAccess(BasePage):

    def __init__(self):
        super().__init__()
        self.base_url = None
        self._pay_plan = None
        self._email = None
        # self.verificationErrors = [] # This is
        # self.accept_next_alert = True

    def collect_login_credentials(self):
        username = input("Please enter a valid Pay Plan:")
        password = input("Please enter a valid Email:")
        self._pay_plan = username
        self._email = password

    def collect_cred_test_access(self, url: str):
        """For the sake of DRY code, we use this function to merge two lines of
        code, that could have otherwise been called in each function that
        handles each site."""
        self.test_site_access(url)
        self.collect_login_credentials()

    def login(self):
        """We do the click and data entry into tables then login below:
        We have 3 sec pause between each input just to ensure the bot
        is not that instant, and we get to see what it actually does.
        Login to: EZPassNJ"""
        from src.ez_pass import EzPassLogin

        self.base_url = "https://www.ezpassnj.com/vector/violations/violationList.do"
        self.collect_cred_test_access(self.base_url)
        EzPassLogin.login_into_ezpass(self)

    def sun_pass_login(self):
        """SunPass Access & Scraping."""
        from src.sunpass_account import SunPassLogin

        self.base_url = 'https://www.sunpass.com/en/home/index.shtml'
        self.collect_cred_test_access(self.base_url)
        SunPassLogin.login_into_sun_pass(self)

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
                WriteToExcel().write_csv_to_excel()
                ScrapeTolls.move_to_next_page(self)
        except Exception as e:
            raise e

    # getter and setter helper methods for the login credentials.
    @property
    def get_email(self):
        return self._email

    @get_email.setter
    def get_email(self, email):
        self._email = email

    @property
    def get_payment_plan(self):
        return self._pay_plan

    @get_payment_plan.setter
    def get_payment_plan(self, new_pay_plan):
        self._pay_plan = new_pay_plan

    def name_files_with_account_date(self):
        """Uses date and account to generate excel file names."""
        from datetime import date
        import ctypes
        today = date.today().isoformat()
        file_name = f'{self.get_payment_plan}-{today}.xlsx'
        return file_name

    def quit_browser(self):
        return self.driver.close()


def main_run():
    process = TollWebsiteAccess()
    process.sun_pass_login()
    print("Your credentials:")
    print(f'Toll Acc: {process.get_payment_plan}')
    print(f'Acc. Mail {process.get_email}')
    print(f':_______________________________* Scrapes *_________________________________')


if __name__ == '__main__':
    main_run()
