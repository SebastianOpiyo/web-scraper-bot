#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Oct 30, 2020
# Date Modified: Nov 10, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet.
# -*- encoding: utf-8 -*-

import csv
from openpyxl import Workbook
from src.base import BasePage


class WriteToExcelExceptions(Exception):
    """Base class that handles all exception in the WriteToExcel class."""
    pass


class EmptyListException(WriteToExcelExceptions):
    """Handles empty list exceptions."""
    pass


class FinalTollProcessingException(WriteToExcelExceptions):
    """Any error exception from final tolls processing."""
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

    @classmethod
    def name_files_with_account_date(cls, payment_plan):
        """Uses date and account to generate excel file names."""
        from datetime import date
        today = date.today().isoformat()
        file_name = f'{payment_plan}-{today}.xlsx'
        print(file_name)
        return file_name

    def write_csv_to_excel(self, payment_plan):
        """Writes csv data to excel sheet.
        - This data is purely row.
        - We can use the @openxlsx methods or this method to achieve the same result."""
        from src.login_script import TollWebsiteAccess
        excel_file = f'./rowtolls/row_excel/{WriteToExcel.name_files_with_account_date(payment_plan)}'
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
                    if result_list[1] == 'License Plate Number':
                        pass
                    else:
                        self.sheet.append(result_list)
            self.wb.save(excel_file)

    def final_ezpasstoll_processing(self, file_name):
        """This methods used the following helper methods to accomplish the processing:
        @method: process_new_toll_row()
        @:return processec excel file
        """
        self.columns = ["LP", "STATE", "DATE-TIME", "AGENCY", "CLIENT", "EXIT-LANE", "CLASS", "AMOUNT"]
        self.sheet.append(self.columns)
        with open('tolls.csv') as csv_data:
            csv.register_dialect(
                'mydialect',
                delimiter=',',
                quotechar='"',
                doublequote=True,
                skipinitialspace=True,
                lineterminator='\n',
                quoting=csv.QUOTE_MINIMAL
            )
            reader = csv.reader(csv_data)
            for row in reader:
                # print(row)
                for i in row[1:]:
                    result_row = i.splitlines()
                    try:
                        if result_row[1] == 'License Plate number':
                            pass
                        else:
                            new_row = WriteToExcel.process_new_toll_row(result_row)
                            self.sheet.append(new_row)
                    except Exception as e:
                        print(f'Encountered the following Error --> {e}')
            self.wb.save(f'./processedtolls/processed_toll_{file_name}.xlsx')

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

        new_row = []
        if not toll_list:
            raise EmptyListException("The toll list is empty, you might have reached the end of the file!")

        if toll_list:
            license_plate, state, date_time, agency, client, exit_lane, toll_class, amount_due = \
                '', '', '', '', '', '', '-', '',
            if toll_list[1] == 'License Plate Number':
                pass
            else:
                date_time = toll_list[2]
                client = 'AMAZON LOGISTICS, INC.'
                license_plate = toll_list[1].split('-')[0]
                if license_plate[1] == 'T':
                    state = 'ID'
                elif license_plate[1] == 'H':
                    state = 'OR'
                else:
                    state = '-'
            try:
                if not toll_list[3]:
                    # check if url exists, if not we append a fake one
                    toll_list[3] = 'http://10.37.248.147/njta/202011/' \
                                   '20201102/18W_09w/01318W_09wW2020110214193143SV_02.jpg'

                splice_toll_agency = toll_list[3].split('/')[3]
                agency = f'{WriteToExcel.check_agency(splice_toll_agency)}'
                exit_lane = f'{splice_toll_agency.upper()} -- {toll_list[4]} '
                amount_due = toll_list[9]
            except Exception as e:
                print(f'Encountered the following Error --> {e}')
            new_row.extend([license_plate, state, date_time, agency, client, exit_lane, toll_class, amount_due])
        return new_row

    @staticmethod
    def check_agency(agency_abbr=None):
        """Given an abbreviation of an agency, it checks for to full name
        from dictionary, if it does exist it assigns the correct one."""
        agency_dict = {'dr': 'DELAWARE DEPARTMENT OF TRANSPORTATION', 'drba': 'DELAWARE RIVER AND BAY AUTHORITY',
                       'drjt': 'DELAWARE RIVER JOINT TOLL BRIDGE COMMISSION', 'njta': 'NEW JERSEY TURNPIKE AUTHORITY'}
        if agency_abbr is None:
            return f'NEW JERSEY TURNPIKE AUTHORITY'
        else:
            for i in agency_dict:
                if i == agency_abbr:
                    return agency_dict.get(i)
