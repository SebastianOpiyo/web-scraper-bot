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
import requests
import time
import psutil

"""After login we have to do the following:
1. Select each row and View Details per rows
2. Scrape the selected View.
3. Convert data into CSV
4. Push data to Amazon s3"""

"""

def get_upcoming_events(url):
    # this is the only line that changes
    # the rest remain the same as in selenium.
    # driver = webdriver.PhantomJS(executable_path='/home/intelligentbots/Projects/web-scraper-bot/phantomjs/')
    # driver.get(url)
    #
    # events = driver.find_elements_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/div/div[6]/h4[3]/b/b')
    #
    # for event in events:
    #     event_details = dict()
    #     event_details['name'] = event.find_element_by_xpath('h3[@class="event-title"]/a').text
    #     event_details['location'] = event.find_element_by_xpath('p/span[@class="event-location"]').text
    #     event_details['time'] = event.find_element_by_xpath('p/time').text
    #     print(event_details)
    # # When done, we don't want to populate our display with lots of open web
    # # browser tabs.
    # driver.close()
"""


class ScrapeTolls(TollWebsiteAccess):

    def __init__(self):
        super().__init__()

    def check_all_boxes(self):
        """Check all the checkboxes in the toll list so as
        to get the dynamically generated data using the web driver."""
        # main_run()
        try:
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.ID, 'checkAll')))
            # check_all_boxes = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/'
            #                                                     'div/div[11]/table/thead/tr/th[1]/div/ins"]')
            # self.driver.execute_script("arguments[0].click();", check_all_boxes)
            self.driver.find_element_by_id('checkAll').click()

            time.sleep(3)

            self.driver.get_screenshot_as_file('check-page.png')

        except Exception as e:
            print(f'Could not check the box because of: {e}')

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

    def move_to_next_page(self):
        try:
            load_page = self.driver.find_element_by_xpath('html/body')
            next_icon = load_page.find_element_by_xpath('//*[@id="sb-site"]/div[3]/div/div/form/div/div[11]/'
                                                        'div[1]/center/a[2]/img')
            self.driver.execute_script("arguments[0].click();", next_icon)
        except Exception as e:
            print(f'Could not move to the next page because of the Error: {e}')

    def create_soup(self):
        pass

    def scrape_the_soup(self):
        pass

    def run(self):
        self.check_all_boxes()


if __name__ == '__main__':
    scraper = ScrapeTolls()
    scraper.run()
    # Checking for the selenium running instances of chrome.
    # c = webdriver.Chrome()
    # c.service.process
    # p = psutil.Process(c.service.process.pid)
    # print(p.children(recursive=True))
