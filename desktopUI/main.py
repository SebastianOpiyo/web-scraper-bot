#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 24, 2020
# Date Modified: Nov 24, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper Desktop UI.
# -*- coding: utf-8 -*-

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

import sys

app = QApplication([])

label = QLabel('Large Scale Toll Scraping Robot!')
label.show()


if __name__ == '__main__':
    app.exec_()
