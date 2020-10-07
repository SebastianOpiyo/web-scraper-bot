#!/bin/python3
# Author: Sebastian Opiyo.
# Date Created: Oct 7, 2020
# Date Modified: Oct 7, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper.
# -*- coding: utf-8 -*-

from selenium import webdriver


"""After login we have to do the following:
1. Select each row and View Details per rows
2. Scrape the selected View.
3. Convert data into CSV
4. Push data to Amazon s3"""

def get_upcoming_events(url):
    # this is the only line that changes
    # the rest remain the same as in selenium.
    driver = webdriver.PhantomJS(executable_path='/home/intelligentbots/Projects/web-scraper-bot/phantomjs/')
    driver.get(url)

    events = driver.find_elements_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/div/div[6]/h4[3]/b/b')

    for event in events:
        event_details = dict()
        event_details['name'] = event.find_element_by_xpath('h3[@class="event-title"]/a').text
        event_details['location'] = event.find_element_by_xpath('p/span[@class="event-location"]').text
        event_details['time'] = event.find_element_by_xpath('p/time').text
        print(event_details)
    # When done, we don't want to populate our display with lots of open web
    # browser tabs.
    driver.close()


if __name__ == '__main__':
    get_upcoming_events('https://www.ezpassnj.com/vector/violations/violationList.do/')
