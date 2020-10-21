#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Oct 7, 2020
# Date Modified: Oct 7, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper.
# -*- coding: utf-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
from Screenshot import Screenshot_Clipping
from src.base import BasePage
# from src.login_script import main_run
import requests
import time
import psutil
import csv

"""After login we have to do the following:
1. Select each row and View Details per rows
2. Scrape the selected View.
3. Convert data into CSV
4. Push data to Amazon s3
"""


class ScrapeTolls(BasePage):
    from src.login_script import TollWebsiteAccess

    def __init__(self):
        super().__init__()

    def check_all_boxes(self):
        """Check all the checkboxes in the toll list so as
        to get the dynamically generated data using the web driver."""
        # currently doesn't fully work as expected.
        try:
            time.sleep(120)
            # WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.ID, 'checkAll')))
            # check_all_boxes = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/'
            #                                                     'div/div[11]/table/thead/tr/th[1]/div/ins"]')
            check_box = self.driver.find_element_by_id('checkAll')
            actions = ActionChains(self.driver)
            actions.move_to_element(check_box).perform()
            self.driver.execute_script("arguments[0].click();", check_box)
            time.sleep(5)
            # self.take_screen_shot('check-page.png')
            print(f'Selected all checkboxes')
        except Exception as e:
            raise e

    def scrape_title_info(self):
        """Scrapes information about the account, i.e:
        - Total Amount Due
        - Open Violation."""
        try:
            # amount_due = self.driver.find_element_by_xpath('//*[@id="sb-site"]/div[3]/div/div/form/div/'
            #                                                'div[9]/div[1]/h4')
            # print(amount_due.text)
            load_page = self.driver.find_elements_by_xpath('html/body')
            acc_details = dict()
            time.sleep(5)
            for item in load_page:
                # print(item.text)
                acc_details['TotalAmountDue'] = item.find_element_by_xpath('//*[@id="sb-site"]/div['
                                                                           '3]/div/div/form/div/ '
                                                                           'div[9]/div[1]/h4').text
                acc_details['OpenViolation'] = item.find_element_by_xpath('//*[@id="sb-site"]/div[3]/div/div/form/'
                                                                          'div/div[9]/div[2]/h4').text
                print(f'Account Details: {acc_details}')
            # # return acc_details
        except Exception as e:
            print(f'Could not acquire title information because of Error: {e}')
            pass

    def scrape_table_rows(self):
        # Scrapes toll data from each row and dumps it into a list
        # The info from the list is then transferred to a csv file.
        # toll_acc = self.scrape_title_info()
        toll_table = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/'
                                                       'form/div/div[11]/table/tbody')
        print(f'Tolls Table Details:')
        # print(f'{table_header}')
        table_body = toll_table.find_elements_by_tag_name('tr')
        for row in table_body:
            print(row.text)
            time.sleep(6)
            tolls = row.find_element_by_partial_link_text('View Details')
            self.driver.execute_script("arguments[0].click();", tolls)
            self.execute_view_detail(self=self)
            # The we collect the data we need.
            # toll_list = []
            # toll_list.append(item)
            # print(toll_list)
            # when done, write it into a csv file.
            # self.write_toll_to_csv(toll_list, toll_acc)
            print(':----------------------------------tolls-------------------------------------:')

    @staticmethod
    def execute_view_detail(self):
        """Calls the javascript View Details function on the table so as to create
        the dynamic content table."""
        try:
            dynamic_table_link = self.driver.find_element_by_xpath('//*[@id="transactionItems"]/tbody')
            rows_details = dynamic_table_link.find_elements_by_tag_name('tr')
            for toll_item in rows_details:
                print('*-------------------------Start Tolls Report/View ----------------------------*')
                print(toll_item.text)
                print('*-------------------------End Tolls Report/View ----------------------------*')
                time.sleep(2)
        except Exception as e:
            print(f'Could not scrape the tolls due to Error: {e}')

    @staticmethod
    def write_toll_to_csv(self, toll_list: list = None, toll_acc: list = None):
        # Writes the title information and tolls scraped into the csv file.
        if toll_list is not list:
            print(f'{toll_list} needs to be a list')
            raise Exception
        else:
            pass

        if toll_acc is not dict:
            print(f'{toll_acc} needs to be a dict')
            raise Exception
        else:
            pass

        with open('tolls.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # write to csv the account details
            if toll_acc:
                for item in toll_acc:
                    csv_writer.writerow(toll_acc[item])
            # write to csv the tolls scrapes
            if toll_list:
                for item in toll_list:
                    csv_writer.writerow(item)

    def take_screen_shot(self, filename: str):
        # Takes the screenshot of what the robot has achieved anonymously.
        # that way we can be able to tell whether the robot is doing what we have programmed it to.
        obj = Screenshot_Clipping.Screenshot()
        img_url = obj.full_Screenshot(self.driver, save_path=r'./screenshots', image_name=f'{filename}')
        print(img_url)

    def move_to_next_page(self):
        # This function targets the image with title=Next.
        try:
            load_page = self.driver.find_element_by_xpath('html/body')
            next_icon = load_page.find_element_by_css_selector("a[title=\"Next\"]")
            self.driver.execute_script("arguments[0].click();", next_icon)
            time.sleep(6)
            print(f'Moved to the next page!')
        except Exception as e:
            print(f'Could not move to the next page because of the Error: {e}')

    def create_soup(self):
        pass

    def scrape_the_soup(self):
        pass

    def exit_driver(self):
        self.driver.quit()


def run_scraper():
    scraper = ScrapeTolls()
    print(f'-*-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TITLE INFO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -*-')
    scraper.scrape_title_info()
    # print(f'-*-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TOLLS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -*-')
    # scraper.scrape_table_rows()


# if __name__ == '__main__':
#     main_run()
#     # run_scraper()

