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
    """
    TXHCTRA = 1
    TXTAG = 2
    CAFASTTRACK = 3
    CATHETOLLROADS = 4
    COEXPRESS = 5
    ILIPASS = 6
    KYRIVERLINK = 7
    NCQUICKPASSNC = 8
    NJEZPASS = 9
    OHEZPASS = 10
    OKPIKEPASS = 11
    PAEZPASS = 12
    WAGOODTOGO = 13


class MainScraperRun:
    """This is the main entry file.
    - It calls all the other modules depending on user needs."""
    pass


def main():
    print(repr(TollSites.TXTAG))
    print(TollSites(3).name)


if __name__ == '__main__':
    main()
