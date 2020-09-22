#!/bin/python3
# Author: Sebastian Opiyo.
# Date Created: Sep 16, 2020
# Date Modified: Sep 16, 2020
# Description: An Amazon Toll Scraping Bot.


from bs4 import BeautifulSoup
import requests


class RequestsErrorHandler(Exception):
    """handles all requests Error Exceptions."""
    pass


class ScrapingBot:
    """Base class for scraping."""
    url = "https://www.ezpassnj.com/vector/violations/" \
          "violationInquiry.do"

    def __init__(self, url):
        self.url = url

    # To be replaced with scrapy implementation.
    def get_new_page(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, 'lxml')
        events = soup.find('ul', {'class': 'list-recent-events'}).findAll('li')

        for event in events:
            event_details = dict()
            event_details['name'] = event.find('h3').find('a').text
            event_details['location'] = event.find('span', {'class', 'event-location'}).text
            event_details['time'] = event.find('time').text
            print(event_details)
