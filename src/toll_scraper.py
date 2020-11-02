#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Oct 7, 2020
# Date Modified: Oct 30, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper.
# -*- coding: utf-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
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


class ScrapeTolls(BasePage):
    from src.login_script import TollWebsiteAccess

    def __init__(self):
        super().__init__()

    def check_next_page(self):
        """Checks for the existence of next page:
        @:param
        @:returns Bool values if it does exist or not."""
        load_page = self.driver.find_element_by_xpath('html/body')
        next_icon = load_page.find_element_by_css_selector("a[title=\"Next\"]")
        if next_icon:
            return True

    def check_all_boxes(self):
        """Check all the checkboxes in the toll list so as
        to get the dynamically generated data using the web driver.
        Note: This is no longer necessary"""
        # currently doesn't fully work as expected.
        try:
            time.sleep(120)
            # WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.ID, 'checkAll')))
            # check_all_boxes = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/'
            #                                                     'div/div[11]/table/thead/tr/th[1]/div/ins"]')
            check_box = self.driver.find_element_by_id('checkAll')
            actions = ActionChains(self.driver)
            actions.move_to_element(check_box).perform()
            self.driver.execute_script("arguments[0].click();", check_box)
            time.sleep(5)
            # self.take_screen_shot('check-page.png')
            print(f'Selected all checkboxes')
        except Exception as e:
            raise e

    def scrape_title_info(self):
        """Scrapes information about the account, i.e:
        - Total Amount Due
        - Open Violation."""
        try:
            load_page = self.driver.find_elements_by_xpath('html/body')
            acc_details = dict()
            time.sleep(3)
            for item in load_page:
                # print(item.text)
                acc_details['TotalAmountDue'] = item.find_element_by_xpath('//*[@id="sb-site"]/div['
                                                                           '3]/div/div/form/div/ '
                                                                           'div[9]/div[1]/h4').text
                acc_details['OpenViolation'] = item.find_element_by_xpath('//*[@id="sb-site"]/div[3]/div/div/form/'
                                                                          'div/div[9]/div[2]/h4').text
                # print(f'Account Details: {acc_details}')
            return acc_details
        except Exception as e:
            print(f'Could not acquire title information because of Error: {e}')
            pass

    def scrape_table_rows(self):
        from src.write_to_excel import WriteToExcel
        from src.login_script import TollWebsiteAccess
        # Scrapes toll data from each row and dumps it into a list
        # The info from the list is then transferred to a csv file.

        acc_name = f'Account Name: {TollWebsiteAccess.get_payment_plan.__str__}\n'
        toll_table = self.driver.find_elements_by_id('transactionItems')
        scrapes_list = []
        for item in toll_table:
            table_body = item.find_elements_by_tag_name('tr')
            string_list = []
            for i in table_body:
                time.sleep(1)
                scrape_item = i.get_attribute('innerText')
                string_list.append(scrape_item)
            scrapes_list.append(string_list)
        # print(scrapes_list)
        ScrapeTolls.write_toll_to_csv(scrapes_list, acc_name)
        # for item in scrapes_list:
        #     WriteToExcel().openxlsx(item)
        # # WriteToExcel.openxlsx(scrapes_list)

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

    def move_to_next_page(self):
        # This function targets the image with title=Next.
        try:
            load_page = self.driver.find_element_by_xpath('html/body')
            next_icon = load_page.find_element_by_css_selector("a[title=\"Next\"]")
            self.driver.execute_script("arguments[0].click();", next_icon)
            time.sleep(6)
            print(f'Moved to the next page!')
        except Exception as e:
            print(f'Could not move to the next page because of the Error: {e}')
