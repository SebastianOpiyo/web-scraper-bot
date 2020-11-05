#!/bin/python3
# Author: Sebastian Opiyo.
# Date Created: Oct 8, 2020
# Date Modified: Oct 8, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper.
# -*- coding: utf-8 -*-

from flask import Flask, request
from login_script import TollWebsiteAccess

app = Flask(__name__)

login_credentials = {}
toll_site_urls = []


@app.route('/')
def homepage():
    return "Hello scraper!"


@app.route('/login', methods=['GET', 'POST'])
def toll_login(pay_plan, email):
    return "Login in into the Tolls site, using the specified credentials.!"


@app.route('/addurls', methods=['GET', 'POST'])
def add_urls(url):
    toll_site_urls.append(url)
    return f'Url {url} added to list{toll_site_urls}'


@app.route('/deleteurls', methods=['GET', 'POST'])
def delete_urls():
    return "Deletes urls from the bank!"


@app.route('/add_login_credentials', methods=['GET', 'POST'])
def add_login_credentials():
    return "Add login credentials!"


@app.route('/delete_login_credentials', methods=['GET', 'POST'])
def delete_login_credentials():
    return "Delete login credentials!"


@app.route('/scrapetolls')
def start_scraping():
    return "Scrape tolls"


@app.route('/processtolls')
def process_tolls():
    return "Process the tolls!"


@app.route('/createqueue', methods=['GET', 'POST'])
def create_queue():
    return "Create que for the tolls!"


@app.route('/pushtoAmazons3', methods=['GET', 'POST'])
def push_to_s3():
    return "Push to amazon s3 for storage."


if __name__ == '__main__':
    app.run(debug=True)
