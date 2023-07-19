import selenium
from selenium import webdriver
import time

# driver_path = 'C:/LSY/SETUP/chromedriver.exe'

myBrowser = webdriver.Chrome()

myBrowser.get('https://www.naver.com')

time.sleep(5)