#!/bin/python3
# Author: Sebastian Opiyo.
# Date Created: Sep 16, 2020
# Date Modified: Sep 16, 2020
# Description: An Amazon Toll Scraping Bot.

"""This application is a micro-service based scraper that is intent to run
both locally and on the cloud.
"""
from enum import Enum
from src.login_script import TollWebsiteAccess


class TollSites(Enum):
    """The following sites are in existence:
    * HCTRA(TX)
    * TX-TAG(TX)
    * FASTTRACK(CA)
    * THE TOLL ROADS(CA)
    * EXPRESS(CO)
    * IPASS(IL)
    * RIVERLINK(KY)
    * NC-QUICKPASS(NC)
    * NJ-EZPASS(NJ)
    * OH-EZPASS(OH)
    * PIKEPASS(OK)
    * PA-EZPASS(PA)
    * GOOD-TO-GO
    * FL-SUNPASS
    """
    TXHCTRA = 1
    TXTAG = 2
    CAFASTTRACK = 3
    CATHETOLLROADS = 4
    COEXPRESS = 5
    ILIPASS = 6
    KYRIVERLINK = 7
    NCQUICKPASS = 8
    NJEZPASS = 9
    OHEZPASS = 10
    OKPIKEPASS = 11
    PAEZPASS = 12
    WAGOODTOGO = 13
    FLSUNPASS = 14


class MainScraperRun:
    """This is the main entry file.
    - It calls all the other modules depending on user needs.

    TODO:
    1. List sites and ask user to enter whichever to scrape
    2. After scraping process and store the results.
    3. NOTE: When doing the cron job, will go from site to site."""

    @staticmethod
    def print_existing_sites():
        """This is for a commandline App.
        - Prints a list of existing sites and lets the user pick."""
        print(f'List of Toll Sites to Pick from:')
        for site in TollSites:
            print(site.name)
        pick_site = input('Pick site to scrape tolls: ')
        # We call respective func per pick.
        # We could do better with a switch statement like implementation
        if not pick_site:
            print('Please Pick one of the listed sites for scraping!')
        if pick_site == 'TXHCTRA':
            TollWebsiteAccess().hctra_login_scraping()
        elif pick_site == 'TXTAG':
            TollWebsiteAccess().txtag_login_scraping()
        elif pick_site == 'CAFASTTRACK':
            TollWebsiteAccess().fast_track_login_and_scraping()
        elif pick_site == 'CATHETOLLROADS':
            TollWebsiteAccess().toll_roads_login_and_scraping()
        elif pick_site == 'COEXPRESS':
            TollWebsiteAccess().coexpress_login_scraping()
        elif pick_site == 'ILIPASS':
            TollWebsiteAccess().ilpass_login_scraping()
        elif pick_site == 'KYRIVERLINK':
            TollWebsiteAccess().river_link_login_and_scraping()
        elif pick_site == 'NCQUICKPASS':
            TollWebsiteAccess().quickpass_login_scraping()
        elif pick_site == 'NJEZPASS':
            TollWebsiteAccess().ez_pass_login()
        elif pick_site == 'OHEZPASS':
            TollWebsiteAccess().oh_ezpass_login_and_scraping()
        elif pick_site == 'OKPIKEPASS':
            TollWebsiteAccess().pikepass_ok_login_scraping()
        elif pick_site == 'PAEZPASS':
            TollWebsiteAccess().pa_ezpass_login_and_scraping()
        elif pick_site == 'WAGOODTOGO':
            TollWebsiteAccess().good_to_go_login_and_scraping()
        elif pick_site == 'FLSUNPASS':
            TollWebsiteAccess().sun_pass_login_and_scraping()

    @staticmethod
    def desktop_main(agency, username, password, startdate, enddate):
        """Entry Point For the desktop Application."""
        scraper = TollWebsiteAccess(username, password, startdate, enddate)
        pick_site = agency
        if pick_site == "HCTRA(TX)":
            scraper.hctra_login_scraping()
        elif pick_site == "TXTAG":
            scraper.txtag_login_scraping()
        elif pick_site == "FASTTRACK(CA)":
            scraper.fast_track_login_and_scraping()
        elif pick_site == "THETOLLROADS(CA)":
            scraper.toll_roads_login_and_scraping()
        elif pick_site == "EXPRESS(CO)":
            scraper.coexpress_login_scraping()
        elif pick_site == "IPASS(IL)":
            scraper.ilpass_login_scraping()
        elif pick_site == "RIVERLINK(KY)":
            scraper.river_link_login_and_scraping()
        elif pick_site == "QUICKPASS(NC)":
            scraper.quickpass_login_scraping()
        elif pick_site == "EZPASS(NJ)":
            scraper.ez_pass_login()
        elif pick_site == "EZPASS(OH)":
            scraper.oh_ezpass_login_and_scraping()
        elif pick_site == "PIKEPASS(OK)":
            scraper.pikepass_ok_login_scraping()
        elif pick_site == "EZPASS(PA)":
            scraper.pa_ezpass_login_and_scraping()
        elif pick_site == "GOODTOGO(WA)":
            scraper.good_to_go_login_and_scraping()
        elif pick_site == "SUNPASS(FL)":
            scraper.sun_pass_login_and_scraping()


def main():
    MainScraperRun().print_existing_sites()


if __name__ == '__main__':
    main()
