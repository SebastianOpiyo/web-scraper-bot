#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Oct 30, 2020
# Date Modified: Nov 2, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet.
# -*- encoding: utf-8 -*-

import csv
from openpyxl import Workbook
from enum import Enum


class WriteToExcel:
    """Writes scrapes to excel Workbook."""

    class Accounts(Enum):
        EZPass_464 = ''
        EZPass_449 = ''
        EZPass_548 = ''

    def __init__(self):
        self.wb = Workbook()
        self.sheet = self.wb.active
        self.columns = [" ", "License Plate Number", "Date & Time", "Facility(Roadway or Bridge)",
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

    def write_csv_to_excel(self, title: str):
        """Writes csv data to excel sheet.
        - We can use the @openxlsx methods or this method to achieve the same result."""
        from src.login_script import TollWebsiteAccess
        excel_file = TollWebsiteAccess().name_files_with_account_date()
        self.sheet.title(title)
        self.sheet.append(self.columns)
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
                self.sheet.append(result_list)
            self.wb.save(excel_file)


if __name__ == '__main__':
    # WriteToExcel().openxlsx()
    pass

