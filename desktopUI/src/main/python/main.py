#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 24, 2020
# Date Modified: Nov 24, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper Desktop UI.
# -*- coding: utf-8 -*-

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from desktopUI.uidesign.scraperobotui import Ui_TollScraperRobot
from PyQt5.QtWidgets import QMainWindow, QApplication

import sys


class MainWindow(QMainWindow, Ui_TollScraperRobot):

    """Main Window."""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
