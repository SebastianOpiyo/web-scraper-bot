#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Sep 21, 2020
# Date Modified: Nov 10, 2020
# Description: An Amazon Toll Scraping Bot: Login page (For EZ-Pass Amazon Accounts).
# -*- coding: utf-8 -*-

"""This file manages login to the sites to be scraped.
It then calls the [toll_scraper] module classes.
"""

from src.base import BasePage


class BotExceptionHandler(Exception):
    """A common base class for other Bot Exception Error handling classes.."""
    pass


class TollWebsiteAccess(BasePage):

    def __init__(self):
        super().__init__()
        self.base_url = None
        self._pay_plan = None
        self._email = None
        self._site_name = None
        self._filename = f'{self._pay_plan}@{self._site_name}'

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

    def ez_pass_login(self):
        """EZPassNJ Access and Scraping."""
        from src.ez_pass import EzPassLogin

        self.base_url = "https://www.ezpassnj.com/vector/violations/violationList.do"
        self._site_name = 'EZ_PassNJ'
        self.collect_cred_test_access(self.base_url)
        EzPassLogin.login_into_ezpass(self)

    def sun_pass_login_and_scraping(self):
        """SunPass Access & Scraping."""
        from src.sunpass_account import SunPassLogin

        self.base_url = 'https://www.sunpass.com/en/home/index.shtml'
        self._site_name = 'SunPass'
        self.collect_cred_test_access(self.base_url)
        SunPassLogin.login_into_sun_pass(self)
        SunPassLogin.scrape_tolls(self)

    def ntta_login_and_scraping(self):
        """NTTA Access and Scraping."""
        from src.Ntta_site import NttaLoginAndSraping
        self.base_url = 'https://csc.ntta.org/olcsc/AuthenticateUser.do'
        self._site_name = 'NTTA'
        self.collect_cred_test_access(self.base_url)
        NttaLoginAndSraping.ntta_login(self)
        NttaLoginAndSraping.scrapping(self)

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

    @property
    def get_file_name(self):
        return self._filename

    @staticmethod
    def call_write_to_excel(payment_plan):
        from src.write_to_excel import WriteToExcel
        WriteToExcel().write_csv_to_excel(payment_plan)


def main_run():
    process = TollWebsiteAccess()
    # process.ntta_login_and_scraping()
    process.ez_pass_login()
    print("Your credentials:")
    print(f'Toll Acc: {process.get_payment_plan}')
    print(f'Acc. Mail {process.get_email}')
    print(f'File Name: {process.get_file_name}')
    print(f':_______________________________* Scrapes *_________________________________')
    # process.call_write_to_excel(process.get_file_name)
    process.quit_driver()


if __name__ == '__main__':
    main_run()
