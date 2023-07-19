html_doc = '''
    <p class="today">오늘</p>
    <p class="tommorow">내일</p>
    <p class="1234">날짜숫자</p>
'''

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc, 'html.parser')
# BeautifulSoup 객체 생성

class_tag = soup.find(class_=re.compile('[0-9]'))
# 정규표현식을 사용하여 숫자가 포함된 class 속성을 가진 태그를 찾음

print(class_tag)
# 찾은 태그 출력