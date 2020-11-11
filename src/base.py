#!/usr/bin/env python3
# Author: Sebastian Opiyo.
# Date Created: Nov 09, 2020
# Date Modified: Nov 11, 2020
# Description: An Amazon Toll Scraping Bot: Module that writes tolls to the excel sheet(Sunpass Account).
# -*- encoding: utf-8 -*-

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
import time


class BasePage:
    """Driver class inherited by all the other classes.
    - It does initiate the chrome driver, chrome browser being the option.
    - It also closes the browser if needed. NB: - It is a good practice to close
    browser instances after use.
    """

    def __init__(self):
        self.save_file_path = './rowtolls/CSV_Downloads'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_experimental_option("prefs",
                                               {"download.default_directory": self.save_file_path,
                                                "download.prompt_for_download": False,
                                                "download.directory_upgrade": True,
                                                "safebrowsing_for_trusted_sources_enabled": False,
                                                "safebrowsing.enabled": False})
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.maximize_window()

    def test_site_access(self, url):
        # Check to see that the site is accessible or not
        # important because the site needs VPN ON to be accessible.
        try:
            self.driver.implicitly_wait(5)
            self.driver.get(url)
            print("Site can be reached!")
        except Exception as e:
            print(f'Site cannot be reached because of {e}')

    def quit_driver(self):
        """Closes all open instances of the browser instances"""
        time.sleep(15)
        self.driver.quit()

    def close_browser(self):
        """Closes the browser that is in ficus."""
        time.sleep(15)
        return self.driver.close()
