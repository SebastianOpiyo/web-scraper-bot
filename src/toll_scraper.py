#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Oct 7, 2020
# Date Modified: Nov 10, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper.
# -*- coding: utf-8 -*-

from Screenshot import Screenshot_Clipping
from src.base import BasePage

import time
import csv
import random
import string

"""After login we have to do the following:
1. Select each row and View Details per rows
2. Scrape the selected View.
3. Convert data into CSV
4. Push data to Amazon s3
"""


class ScrapingExceptionHandler(Exception):
    """A base class that handles all the exception during scraping."""
    pass


class PageNavigationErrorHandler(ScrapingExceptionHandler):
    """Handles all errors emanating from page-page navigation."""
    pass


class ScrapeTolls(BasePage):
    from src.login_script import TollWebsiteAccess

    def __init__(self):
        super().__init__()
        self.start_date = None
        self.end_date = None

    # By defining start and end date, we get the flexibility of altering any
    # in case of need for change.
    # Note: What about use of setter & getter methods?
    def stop_at_given_date(self):
        """Set Stop scraping tolls at a given date."""
        stop_date = input('Enter Tolls Scrape Stop Date: ')
        self.end_date = stop_date

    def start_at_given_date(self):
        """Set Start at a given date."""
        starting_date = input('Enter Tolls Scrape Start Date: ')
        self.start_date = starting_date

    @property
    def get_start_date(self):
        """Return start date"""
        return self.start_date

    @property
    def get_end_date(self):
        """Return start date"""
        return self.end_date

    def scrape_title_info(self):
        """Scrapes information about the account, i.e:
        - Total Amount Due
        - Open Violation.
        """
        try:
            load_page = self.driver.find_elements_by_xpath('html/body')
            acc_details = dict()
            time.sleep(3)
            for item in load_page:
                acc_details['TotalAmountDue'] = item.find_element_by_xpath('//*[@id="sb-site"]/div['
                                                                           '3]/div/div/form/div/ '
                                                                           'div[9]/div[1]/h4').text
                acc_details['OpenViolation'] = item.find_element_by_xpath('//*[@id="sb-site"]/div[3]/div/div/form/'
                                                                          'div/div[9]/div[2]/h4').text
            return acc_details
        except Exception as e:
            print(f'Could not acquire title information because of Error: {e}')
            pass

    def scrape_table_rows(self):
        # Scrapes toll data from each row and dumps it into a list
        # The info from the list is then transferred to a csv file.
        # page_notation = f'End-Page---*---New page\n'
        toll_table = self.driver.find_elements_by_id('transactionItems')
        scrapes_list = []
        for item in toll_table:
            table_body = item.find_elements_by_tag_name('tr')
            string_list = []
            for i in table_body:
                time.sleep(1)
                scrape_item = i.get_attribute('innerText')
                if scrape_item:
                    string_list.append(scrape_item)
                else:
                    scrape_item = None
                    string_list.append(scrape_item)
            scrapes_list.append(string_list)
        ScrapeTolls.write_toll_to_csv(scrapes_list)

    @staticmethod
    def write_toll_to_csv(toll_list: list = None, toll_acc: str = None):
        """@:param toll_list - a collection of toll scrapes per page.
           @:param toll_acc - a string indicating which acc is being scraped.
           - Description: Writes the title information and tolls scraped into the csv file
        """
        with open('tolls.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, dialect="excel")
            # write to csv the account details
            if toll_acc:
                csv_file.write(toll_acc)
            # write to csv the tolls scrapes
            if toll_list:
                for item in toll_list:
                    print(item)
                    csv_writer.writerow(item)

    def take_screen_shot(self, filename: str):
        # Takes the screenshot of what the robot has achieved anonymously.
        # that way we can be able to tell whether the robot is doing what we have programmed it to.
        obj = Screenshot_Clipping.Screenshot()
        img_url = obj.full_Screenshot(self.driver, save_path=r'./screenshots', image_name=f'{filename}')
        print(img_url)

    @staticmethod
    def random_filename_generator():
        # Generates random strings, used for file name.
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10))
        return f'{name}.png'

    def check_next_page(self):
        """Checks for the existence of next page in the EZ_Pass Acc.:
        @:returns Bool values if it does exist or not.
        """

        load_page = self.driver.find_element_by_xpath('html/body')
        next_icon = load_page.find_element_by_css_selector("a[title=\"Next\"]")
        if next_icon:
            return True
        elif not next_icon:
            time.sleep(10)
            try:
                if next_icon:
                    return True
            except Exception as e:
                print(f'The bot could not move to the next page due to {e}')

    def move_to_next_page(self):
        # This function targets the image with title=Next in the EZ_Pass Acc..
        try:
            load_page = self.driver.find_element_by_xpath('html/body')
            next_icon = load_page.find_element_by_css_selector("a[title=\"Next\"]")
            self.driver.execute_script("arguments[0].click();", next_icon)
            time.sleep(6)
            print(f'Moved to the next page!')
        except Exception as e:
            print(f'Could not move to the next page because of the Error: {e}')


if __name__ == "__main__":
    scraper_instance = ScrapeTolls()
    scraper_instance.start_at_given_date()
    scraper_instance.stop_at_given_date()
    start_date = scraper_instance.get_start_date
    end_date = scraper_instance.get_end_date
    print(start_date, end_date)
