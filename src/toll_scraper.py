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
        self.driver.implicitly_wait(30)
        main_run()
        try:
            wait = WebDriverWait(self.driver, 30)
            check_all = wait.until(EC.element_to_be_clickable((By.ID, 'checkAll')))
            check_all_boxes = self.driver.find_element_by_id('checkAll')
            self.driver.execute_script("arguments[0].click();", check_all_boxes)
        except Exception as e:
            print(e)

    def move_to_next_page(self):
        pass

    def create_soup(self):
        pass

    def scrape_the_soup(self):
        pass

    def run(self):
        self.check_all_boxes()
        self.driver.get_screenshot_as_file('check-page.png')


if __name__ == '__main__':
    scraper = ScrapeTolls()
    scraper.run()
    # Checking for the selenium running instances of chrome.
    # c = webdriver.Chrome()
    # c.service.process
    # p = psutil.Process(c.service.process.pid)
    # print(p.children(recursive=True))
