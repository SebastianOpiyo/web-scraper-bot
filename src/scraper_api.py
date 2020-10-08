#!/bin/python3
# Author: Sebastian Opiyo.
# Date Created: Oct 8, 2020
# Date Modified: Oct 8, 2020
# Description: An Amazon Toll Scraping Bot: Toll scraper.
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Hello scraper!"


@app.route('/login', methods=['GET', 'POST'])
def toll_login():
    return "Login in into the Tolls site!"


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
