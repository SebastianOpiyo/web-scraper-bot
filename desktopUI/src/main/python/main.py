#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 24, 2020
# Date Modified: Nov 24, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper Desktop UI.
# -*- coding: utf-8 -*-

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Window(QMainWindow):

    """Main Window."""

    def __init__(self, *args, **kwargs):
        """Initializer."""
        super(QMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Toll Scraper Robot')

        self.setFixedSize(600, 350)
        # set the central widget
        self._centralWidget = QWidget(self)
        # Set menu
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        self._createComboBox()
        self._createpushbuttons()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createComboBox(self):
        combo = QComboBox()
        combo.addItems(["SUNPASS(FL)", "GOODTOGO(WA)", "EZPASS(PA)", "PIKEPASS(OK)", "EZPASS(OH)", "EZPASS(NJ)",
                             "QUICKPASS(NC)", "RIVERLINK(KY)", "IPASS(IL)", "EXPRESS(CO)", "THETOLLROADS(CA)",
                             "FASTTRACK(CA)", "TXTAG", "HCTRA(TX)"])
        self.setCentralWidget(combo)

    def _createpushbuttons(self):
        pass

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Ready!")
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
