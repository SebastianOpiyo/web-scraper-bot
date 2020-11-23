#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 23, 2020
# Date Modified: Nov 23, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper Desktop UI.
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel('Large Scale Toll Scraping Robot!')
label.show()

# app.exec_()

if __name__ == '__main__':
    app.exec_()
