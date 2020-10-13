#!/bin/python3
# Author: Sebastian Opiyo.
# Date Created: Oct 13, 2020
# Date Modified: Oct 13, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper.
# -*- coding: utf-8 -*-

"""This script handles the dynamic data generation.
Especially, the table links that need to be clicked to generate
toll information.
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebPage
from lxml import html


class Render(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _load_finished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()


url = 'http://pycoders.com/archive/'
r = Render(url)
result = r.frame.toHtml()
htmltree = html.fromstring(result)
archive_links = htmltree.xpath('//div[2]/div[2]/div/div[@class="campaign"]/a/@href')
print(archive_links)
