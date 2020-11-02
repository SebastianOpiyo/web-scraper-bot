#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Oct 7, 2020
# Date Modified: Oct 30, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet.
# -*- encoding: utf-8 -*-

import csv
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
        """Writes scraped tolls directly to excel."""
        # self.sheet.title('Amazon Tolls Scrapes.')
        # self.sheet.append(self.columns)
        for toll in toll_list:
            for i in toll:
                result_list = i.splitlines()
            # self.sheet.append(result_list)
        self.wb.save(self.filename)

    def write_csv_to_excel(self):
        csv.register_dialect(
            'mydialect',
            delimiter=',',
            quotechar='"',
            doublequote=True,
            skipinitialspace=True,
            lineterminator='\n',
            quoting=csv.QUOTE_MINIMAL
        )

        with open('tolls.csv') as file:
            reader = csv.reader(file, dialect='mydialect')
            for row in reader:
                for i in row:
                    result_list = i.splitlines()
                    # print(result_list)
                self.sheet.append(result_list)
            self.wb.save('csvToExcel.xlsx')


if __name__ == '__main__':
    # WriteToExcel().openxlsx()
    WriteToExcel().write_csv_to_excel()
