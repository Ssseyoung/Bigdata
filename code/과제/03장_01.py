'''
문제 1
URL = 'https://serieson.naver.com/v3/movie/products/action?sortType=UPDATE_DESC&price=all&#39; 
에 접속하여 html_data 를 가져온 후 장르 목록을 찾아서 모두 출력하시오
'''
import requests
from bs4 import BeautifulSoup

URL = 'https://serieson.naver.com/v3/movie/products/action?sortType=UPDATE_DESC&price=all'

req = requests.get(URL)
html_data = req.content
soup = BeautifulSoup(html_data, 'html.parser')

genre_list = soup.select('.CategoryTab_link___LUFe')

for genre in genre_list:
    print(genre.text.strip())
    
# 문제 2번 링크는 열리지 않습니다.