#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Oct 7, 2020
# Date Modified: Oct 30, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet.
# -*- encoding: utf-8 -*-


from openpyxl import Workbook


class WriteToExcel:
    """Writes scrapes to excel Workbook."""

    def __init__(self):
        self.wb = Workbook()
        self.sheet = self.wb.active
        self.columns = ["License Plate Number", "Date & Time", "Facility(Roadway or Bridge)",
                        "Interchange# - Toll Plaza", "Status*", "Toll", "Fee", "NSF Fee", "Amt Due"]
        self.filename = "tolls.xlsx"

    def openxlsx(self, toll_list: list):
        # self.sheet.title('Amazon Tolls Scrapes.')
        self.sheet.append(self.columns)
        for toll in toll_list:
            self.sheet.append(toll)
        self.wb.save(self.filename)


if __name__ == '__main__':
    WriteToExcel().openxlsx()