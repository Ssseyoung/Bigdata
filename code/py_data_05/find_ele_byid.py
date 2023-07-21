import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = 'https://shoemuf.com/member/join.html'

webdriver = webdriver.Chrome()

webdriver.get(URL)

ele_btn = webdriver.find_element(By.ID, 'postBtn')  
# ele_btn 변수에 'postBtn' ID를 가진 요소를 찾아서 할당한다.

# print(ele_btn.tag_name)
# print(ele_btn.text)

ele_menus = webdriver.find_elements(By.CLASS_NAME, 'xans-record-')  
# 'xans-record-' 클래스 이름을 가진 요소들을 찾아서 ele_menus 변수에 할당한다.
for el_menu in ele_menus:
    print(el_menu.text)
    
time.sleep(10)
