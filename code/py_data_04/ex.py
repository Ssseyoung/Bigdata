# 네이트 실시간 이슈 키워드

from bs4 import BeautifulSoup
import requests
import re

URL = 'https://www.nate.com/'
response = requests.get(URL)

html_doc = response.text 
# print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify)

div_isKeyword = soup.find('div', class_='isKeyword')  
# div 태그 중 class가 'isKeyword'인 요소를 찾음
h4 = div_isKeyword.select_one('h4')  
# div_isKeyword에서 h4 태그를 선택
# print(h4.string)

lies = div_isKeyword.find_all('li')  
# div_isKeyword에서 모든 li 태그를 찾음
# print(len(lies))
for li in lies:
    rank = li.select_one('span.num_rank')  
    # li 태그 내에서 class가 'num_rank'인 span 태그를 선택
    print(rank.string, '위', end=' ')  
    # rank의 문자열과 '위'를 출력하고 줄바꿈하지 않음
    text = li.select_one('span.num_rank')  
    # li 태그 내에서 class가 'num_rank'인 span 태그를 선택
    print(text.string)