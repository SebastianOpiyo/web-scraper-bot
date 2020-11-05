#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Oct 30, 2020
# Date Modified: Nov 2, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet.
# -*- encoding: utf-8 -*-

import csv
from openpyxl import Workbook
from src.base import BasePage
from enum import Enum


class WriteToExcelExecptions(Exception):
    """Base class that handles all exception in the WriteToExcel class."""
    pass


class EmptyListException(WriteToExcelExecptions):
    """Handles empty list exceptions."""
    pass


class WriteToExcel(BasePage):
    """Writes scrapes to excel Workbook."""

    def __init__(self):
        super().__init__()
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

    def write_csv_to_excel(self):
        """Writes csv data to excel sheet.
        - This data is purely row.
        - We can use the @openxlsx methods or this method to achieve the same result."""
        from src.login_script import TollWebsiteAccess
        excel_file = TollWebsiteAccess().name_files_with_account_date()
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

        with open('tolls.csv', 'r') as file:
            reader = csv.reader(file, dialect='mydialect')
            for row in reader:
                for i in row:
                    result_list = i.splitlines()
                self.sheet.append(result_list)
            self.wb.save(excel_file)

    def final_ezpasstoll_processing(self):

        self.columns = ["LP", "STATE", "DATETIME", "AGENCY", "CLIENT", "EXIT-LANE", "CLASS", "AMOUNT"]
        self.sheet.append(self.columns)

        with open('tolls.csv') as csv_data:
            reader = csv.reader(csv_data)
            for row in reader:
                for i in row:
                    result_row = i.splitlines()

                    print(result_row[2])

            # self.wb.save('processed_toll.xlsx')

    @staticmethod
    def process_new_toll_row(toll_list: list):
        """Creates a newly processed row that will be written to the final excel sheet.
                Note: This method processes fully the row data in csv into a final product.
                Header Info: LP = Licence Plate
                     STATE - H = OR, T - ID
                     DATETIME = Date time (Month/Date/Year HH/MM/SS)
                     AGENCY = Agency full name from link abbreviation.
                     CLIENT = AMAZON LOGISTICS, INC.
                     EXIT - (Agency Abbrv -- Interchange# - Toll Plaza
                     CLASS - (Default=5)
                     AMOUNT - Amount Due
        """
        license_plate, state, date_time, agency, client, exit_lane, toll_class, amount_due = \
            '', '', '', '', '', '', '', '',

        new_row = []
        if not toll_list:
            raise EmptyListException("The toll list is empty, you might have reached the end of the file!")

        if toll_list:
            if toll_list[1] == 'License Plate Number':
                pass
            else:
                date_time = toll_list[2]
                client = 'AMAZON LOGISTICS, INC.'
                license_plate = toll_list[1].split('-')[0]
                if license_plate[0] == 'T':
                    state = 'ID'
                else:
                    state = 'OR'

    def stop_at_given_date(self):
        pass

    def check_agency(self, agency_abbr):
        agency_dict = {'dr': 'DELAWARE DEPARTMENT OF TRANSPORTATION', 'drba': 'DELAWARE RIVER AND BAY AUTHORITY',
                       'drjt': 'DELAWARE RIVER JOINT TOLL BRIDGE COMMISSION', 'njta': 'NEW JERSEY TURNPIKE AUTHORITY'}

        for i in agency_dict:
            if i == agency_dict:
                return agency_dict.get(i)



if __name__ == '__main__':
    # WriteToExcel().final_ezpasstoll_processing()
    WriteToExcel().check_agency()

