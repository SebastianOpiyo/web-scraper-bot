# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_TollScraperRobot(object):
    """Main GUI window. """

    def setupUi(self, TollScraperRobot):
        TollScraperRobot.setObjectName("TollScraperRobot")
        TollScraperRobot.resize(800, 599)

        self.centralwidget = QtWidgets.QWidget(TollScraperRobot)
        self.centralwidget.setObjectName("centralwidget")
        self.startscraper = QtWidgets.QPushButton(self.centralwidget)
        self.startscraper.setGeometry(QtCore.QRect(190, 360, 131, 27))
        self.startscraper.setObjectName("startscraper")
        self.stopscraper = QtWidgets.QPushButton(self.centralwidget)
        self.stopscraper.setGeometry(QtCore.QRect(540, 360, 141, 27))
        self.stopscraper.setObjectName("stopscraper")
        self.viewfiles = QtWidgets.QPushButton(self.centralwidget)
        self.viewfiles.setGeometry(QtCore.QRect(540, 430, 141, 27))
        self.viewfiles.setObjectName("viewfiles")
        self.mailtolls = QtWidgets.QPushButton(self.centralwidget)
        self.mailtolls.setGeometry(QtCore.QRect(190, 430, 131, 27))
        self.mailtolls.setObjectName("mailtolls")
        self.Agency_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Agency_comboBox.setGeometry(QtCore.QRect(320, 130, 221, 27))
        self.Agency_comboBox.setObjectName("Agency_comboBox")
        self.start_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.start_dateEdit.setGeometry(QtCore.QRect(130, 290, 191, 28))
        self.start_dateEdit.setProperty("showGroupSeparator", True)
        self.start_dateEdit.setCalendarPopup(True)
        self.start_dateEdit.setObjectName("start_dateEdit")
        self.end_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.end_dateEdit.setGeometry(QtCore.QRect(540, 290, 191, 28))
        self.end_dateEdit.setCalendarPopup(True)
        self.end_dateEdit.setObjectName("end_dateEdit")
        self.agency_label = QtWidgets.QLabel(self.centralwidget)
        self.agency_label.setGeometry(QtCore.QRect(260, 130, 61, 21))
        self.agency_label.setObjectName("agency_label")
        self.startdate_label = QtWidgets.QLabel(self.centralwidget)
        self.startdate_label.setGeometry(QtCore.QRect(50, 290, 91, 19))
        self.startdate_label.setObjectName("startdate_label")
        self.enddate_label = QtWidgets.QLabel(self.centralwidget)
        self.enddate_label.setGeometry(QtCore.QRect(450, 290, 71, 19))
        self.enddate_label.setObjectName("enddate_label")
        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.titlelabel.setGeometry(QtCore.QRect(250, 0, 291, 51))
        self.titlelabel.setObjectName("titlelabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 220, 191, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(540, 220, 191, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 220, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 220, 81, 20))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(130, 520, 601, 23))
        self.progressBar.setProperty("value", 3)
        self.progressBar.setObjectName("progressBar")
        TollScraperRobot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TollScraperRobot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuopen = QtWidgets.QMenu(self.menuFile)
        self.menuopen.setObjectName("menuopen")
        self.menuview = QtWidgets.QMenu(self.menubar)
        self.menuview.setObjectName("menuview")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        TollScraperRobot.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TollScraperRobot)
        self.statusbar.setObjectName("statusbar")
        TollScraperRobot.setStatusBar(self.statusbar)
        self.actionclose = QtWidgets.QAction(TollScraperRobot)
        self.actionclose.setObjectName("actionclose")
        self.actionFile = QtWidgets.QAction(TollScraperRobot)
        self.actionFile.setObjectName("actionFile")
        self.actionFolder = QtWidgets.QAction(TollScraperRobot)
        self.actionFolder.setObjectName("actionFolder")
        self.actionMaximize = QtWidgets.QAction(TollScraperRobot)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionMinimize = QtWidgets.QAction(TollScraperRobot)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionAbout_Robot = QtWidgets.QAction(TollScraperRobot)
        self.actionAbout_Robot.setObjectName("actionAbout_Robot")
        self.actionversion = QtWidgets.QAction(TollScraperRobot)
        self.actionversion.setObjectName("actionversion")

        self.menuopen.addAction(self.actionFile)
        self.menuopen.addAction(self.actionFolder)
        self.menuFile.addAction(self.actionclose)
        self.menuFile.addAction(self.menuopen.menuAction())
        self.menuview.addAction(self.actionMaximize)
        self.menuview.addAction(self.actionMinimize)
        self.menuHelp.addAction(self.actionAbout_Robot)
        self.menuHelp.addAction(self.actionversion)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuview.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(TollScraperRobot)
        QtCore.QMetaObject.connectSlotsByName(TollScraperRobot)

    def retranslateUi(self, TollScraperRobot):
        _translate = QtCore.QCoreApplication.translate
        TollScraperRobot.setWindowTitle(_translate("TollScraperRobot", "Gravitas Business Solution Ltd."))
        # TollScraperRobot.setStatusBar(_translate("TollScraperRobot", "Ready!"))
        self.Agency_comboBox.addItems(["SUNPASS(FL)", "GOODTOGO(WA)", "EZPASS(PA)", "PIKEPASS(OK)", "EZPASS(OH)",
                                       "EZPASS(NJ)", "QUICKPASS(NC)", "RIVERLINK(KY)", "IPASS(IL)", "EXPRESS(CO)",
                                       "THETOLLROADS(CA)", "FASTTRACK(CA)", "TXTAG", "HCTRA(TX)"])
        self.statusbar.showMessage('Robot Ready!')

        self.startscraper.setText(_translate("TollScraperRobot", "Start Scraper"))
        self.stopscraper.setText(_translate("TollScraperRobot", "Stop Scraper"))

        self.viewfiles.setText(_translate("TollScraperRobot", "View Files"))
        self.mailtolls.setText(_translate("TollScraperRobot", "Mail Tolls"))
        self.start_dateEdit.setDisplayFormat(_translate("TollScraperRobot", "MM/dd/yyyy"))
        self.end_dateEdit.setDisplayFormat(_translate("TollScraperRobot", "MM/dd/yyyy"))
        self.agency_label.setText(_translate("TollScraperRobot", "Agency"))
        self.startdate_label.setText(_translate("TollScraperRobot", "Start Date"))
        self.enddate_label.setText(_translate("TollScraperRobot", "End Date"))
        self.titlelabel.setText(_translate("TollScraperRobot", "<html><head/><body><p align=\"center\"><span style=\" "
                                                               "font-size:22pt; font-weight:600;\">"
                                                               "Toll Scraping Robot</span></p></body></html>"))
        self.label.setText(_translate("TollScraperRobot", "User name"))
        self.label_2.setText(_translate("TollScraperRobot", "Password"))
        self.menuFile.setTitle(_translate("TollScraperRobot", "File"))
        self.menuopen.setTitle(_translate("TollScraperRobot", "open"))
        self.menuview.setTitle(_translate("TollScraperRobot", "view"))
        self.menuHelp.setTitle(_translate("TollScraperRobot", "Help"))

        self.actionclose.setText(_translate("TollScraperRobot", "close"))
        self.actionclose.triggered.connect(self.exit_window)

        self.actionFile.setText(_translate("TollScraperRobot", "File"))
        self.actionFolder.setText(_translate("TollScraperRobot", "Folder"))
        self.actionMaximize.setText(_translate("TollScraperRobot", "Maximize"))
        self.actionMinimize.setText(_translate("TollScraperRobot", "Minimize"))
        self.actionAbout_Robot.setText(_translate("TollScraperRobot", "About Robot"))
        self.actionversion.setText(_translate("TollScraperRobot", "version"))

    # Helper functions
    def exit_window(self):
        close = QtWidgets.QMessageBox.question(self, "QUIT?",
                                               "Are you sure want to STOP and EXIT?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass
