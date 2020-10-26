#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Oct 7, 2020
# Date Modified: Oct 23, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper.
# -*- coding: utf-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
from Screenshot import Screenshot_Clipping
from base import BasePage
# from src.login_script import main_run
import requests
import time
import psutil
import csv
import random
import string

"""After login we have to do the following:
1. Select each row and View Details per rows
2. Scrape the selected View.
3. Convert data into CSV
4. Push data to Amazon s3
"""


class ScrapeTolls(BasePage):
    from login_script import TollWebsiteAccess

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
            load_page = self.driver.find_elements_by_xpath('html/body')
            acc_details = dict()
            time.sleep(3)
            for item in load_page:
                # print(item.text)
                acc_details['TotalAmountDue'] = item.find_element_by_xpath('//*[@id="sb-site"]/div['
                                                                           '3]/div/div/form/div/ '
                                                                           'div[9]/div[1]/h4').text
                acc_details['OpenViolation'] = item.find_element_by_xpath('//*[@id="sb-site"]/div[3]/div/div/form/'
                                                                          'div/div[9]/div[2]/h4').text
                print(f'Account Details: {acc_details}')
            # return acc_details
        except Exception as e:
            print(f'Could not acquire title information because of Error: {e}')
            pass

    def scrape_table_rows(self):
        div_container = self.driver.find_element_by_xpath('//div[@id="violdtl0" and @class="modal.fade"]')
        print(div_container)

    @staticmethod
    def write_toll_to_csv(self, toll_list: list = None, toll_acc: list = None):
        # Thinking of making this a class method.
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

    @staticmethod
    def random_filename_generator():
        # Generates random strings, used for file name.
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10))
        return f'{name}.png'

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
