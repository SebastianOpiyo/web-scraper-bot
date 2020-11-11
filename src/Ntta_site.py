#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 09, 2020
# Date Modified: Nov 10, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet(Sunpass Account).
# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

BROWSER = webdriver.Firefox(executable_path=r'.\gecko\geckodriver.exe')


def main():
    login()


def login():
    BROWSER.get('https://csc.ntta.org/olcsc/AuthenticateUser.do')
    time.sleep(10)
    user_id = input('Enter User ID: ')
    password_id = input('Enter Password: ')
    form_user_id = BROWSER.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[1]'
                                                 '/div[4]/form/div/div/input[1]')
    form_user_id.send_keys(user_id)
    form_passd = BROWSER.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[1]'
                                               '/div[4]/form/div/div/input[2]')
    form_passd.send_keys(password_id)
    login_button = BROWSER.find_element_by_xpath('//*[@id="loginButton"]').click()
    scrapping()


def scrapping():
    time.sleep(2)
    BROWSER.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/ul/li[2]/a/span').click()
    time.sleep(2)
    start_date = BROWSER.find_element_by_name('startDate')
    end_date = BROWSER.find_element_by_name('endDate')

    input_start = input('Enter start date')
    input_end = input('Enter end date')

    start_date.clear()
    end_date.clear()
    start_date.send_keys(input_start)
    end_date.send_keys(input_end)

    select = Select(BROWSER.find_element_by_name('transactionType'))
    select.select_by_visible_text('Toll')
    BROWSER.find_element_by_id('displayButton').click()


def browser_quit():
    time.sleep(5)
    BROWSER.quit()


if __name__ == '__main__':
    main()
    browser_quit()
