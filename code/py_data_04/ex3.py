from bs4 import BeautifulSoup
import requests
import re

URL = 'https://www.melon.com/chart/week/index.htm'
headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
response = requests.get(URL, headers=headers) 
if response.status_code==200:
    print('접속 성공')
    html_doc = response.text
    
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
div_genres = soup.find('div', class_='wrap_tabmenu_sub')  
# div 태그 중 class가 'warp_tabmenu_sub'인 요소를 찾아서 div_genres 변수에 할당
dd_genres = div_genres.find_all('dd')
urls = {}
for dd_denres in dd_genres:
    lies = dd_denres.select('li')
    for li in lies:
        gname = li.get_text().strip()
        key = gname
        URL = 'http://www.melon.com' + li.find('a').get('href').strip()
        value = URL
        urls[key] = value
print(urls)
    
