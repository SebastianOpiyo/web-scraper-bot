#!/bin/python3
# Author: Sebastian Opiyo.
# Date Created: Oct 7, 2020
# Date Modified: Oct 7, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper.
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
from login_script import TollWebsiteAccess, main_run
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Screenshot import Screenshot_Clipping


import requests
import time
import psutil
import csv

"""After login we have to do the following:
1. Select each row and View Details per rows
2. Scrape the selected View.
3. Convert data into CSV
4. Push data to Amazon s3
"""


class ScrapeTolls(TollWebsiteAccess):

    def __init__(self):
        super().__init__()

    def check_all_boxes(self):
        """Check all the checkboxes in the toll list so as
        to get the dynamically generated data using the web driver."""
        # main_run()
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
        load_page = self.driver.find_element_by_xpath('html/body')
        acc_details = dict()
        acc_details['TotalAmountDue'] = load_page.find_element_by_xpath('//*[@id="sb-site"]/div[3]/div/div/form/div/'
                                                                        'div[9]/div[1]/h4').text
        acc_details['OpenViolation'] = load_page.find_element_by_xpath('//*[@id="sb-site"]/div[3]/div/div/form/'
                                                                       'div/div[9]/div[2]/h4').text
        print(f'Account Details: {acc_details}')

    def scrape_table_rows(self):
        toll_table = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/'
                                                       'form/div/div[11]/table')
        table_header = toll_table.find_element_by_xpath('//*[@id="violationTable"]/thead/tr').text
        print(f'Tolls Table Details:')
        print(f'{table_header}')
        table_body = self.driver.find_element_by_xpath('//*[@id="violationTable"]/tbody')
        for row in table_body:
            toll_list = []
            # The xpath is not certain the correct one.
            item = row.find_element_by_xpath('//*[@id="violationTable"]/tbody/tr').text
            toll_list.append(item)
            # when done, write it into a csv file.
            self.write_toll_to_csv(toll_list)

    @staticmethod
    def write_toll_to_csv(toll_list=None, toll_acc=None):
        if toll_list is not list:
            print(f'{toll_list} needs to be a list')
            raise Exception
        else:
            pass

        if toll_acc is not dict:
            print(f'{toll_acc} needs to be a dict')
            raise Exception
        else:
            pass

        with open('tolls.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # write to csv the account details
            if toll_acc:
                for item in toll_acc:
                    csv_writer.writerow(toll_acc[item])
            # write to csv the tolls scrapes
            if toll_list:
                for item in toll_list:
                    csv_writer.writerow(item)

    def execute_view_detail(self):
        """Calls the javascript View Details function on the table so as to create
        the dynamic content table."""
        pass

    def take_screen_shot(self, filename: str):
        # Takes the screenshot of what the robot has achieved anonymously.
        # that way we can be able to tell whether the robot is doing what we have programmed it to.
        obj = Screenshot_Clipping.Screenshot()
        img_url = obj.full_Screenshot(self.driver, save_path=r'./screenshots', image_name=f'{filename}')
        print(img_url)

    def move_to_next_page(self):
        # since next page is an img link we need to find a way to substitute the
        # number a[n] with the correct page number.
        # by default n=1, so we need to increment it by 1 after every page move.
        # on page 1 n=2 and on page 2 n=3 etc.
        try:
            load_page = self.driver.find_element_by_xpath('html/body')
            next_icon = load_page.find_element_by_xpath('//*[@id="sb-site"]/div[3]/div/div/form/div/div[11]/'
                                                        'div[1]/center/a[2]/img')
            self.driver.execute_script("arguments[0].click();", next_icon)
            time.sleep(6)
            print(f'Moved to the next page!')
        except Exception as e:
            print(f'Could not move to the next page because of the Error: {e}')

    def create_soup(self):
        pass

    def scrape_the_soup(self):
        pass

    def run(self):
        self.check_all_boxes()

    def exit_driver(self):
        self.driver.quit()


if __name__ == '__main__':
    scraper = ScrapeTolls()
    scraper.run()
    # Checking for the selenium running instances of chrome.
    # c = webdriver.Chrome()
    # c.service.process
    # p = psutil.Process(c.service.process.pid)
    # print(p.children(recursive=True))
