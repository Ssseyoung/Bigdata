import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 검색어 : 이순신

driver = webdriver.Chrome()

URL = 'https://www.youtube.com/'
driver.implicitly_wait(10)  # 드라이버에게 암묵적으로 10초 동안 대기하도록 지시 

driver.get(URL)

# input_search = driver.find_element(By.CLASS_NAME, 'style-scope ytd-searchbox')
input_search = driver.find_element(By.NAME, 'search_query')

input_search.click()
input_search.send_keys('이순신')

btn_search = driver.find_element(By.ID, 'search-icon-legacy')
btn_search.click()

# input_search.send_keys(Keys.ENTER)

time.sleep(5)