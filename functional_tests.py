from selenium import webdriver
import os

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title