from bs4 import BeautifulSoup
import requests
import re

URL = 'https://autobuff.co.kr/1962/'
response = requests.get(URL)

html_doc = response.text 
soup = BeautifulSoup(html_doc, 'html.parser')

title = soup.find('h1', class_='post-title')
print(title.string)
ranks = soup.select('h2.wp-block-heading')
# print(len(ranks))
# for rank in ranks:
#     print(rank)

# 1
for i in range(len(ranks)):
    # print(ranks[i].string)
    if i == 3:
        st_str = str(ranks[3])  
        en_str = str(ranks[4])  
        st_pos = html_doc.find(st_str)  
        en_pos = html_doc.find(en_str) 
        p_doc = html_doc[st_pos:en_pos]  
        soup_p = BeautifulSoup(p_doc, 'html.parser')  
        ranks2 = soup_p.select('p')
        print(ranks2[1].string)
        print(ranks2[3].string)


# 2
st_str = str(ranks[3])  # ranks 리스트의 3번째 요소를 문자열로 변환하여 st_str 변수에 저장
en_str = str(ranks[4])  # ranks 리스트의 4번째 요소를 문자열로 변환하여 n_str 변수에 저장
st_pos = html_doc.find(st_str)  # html_doc에서 st_str의 첫 번째 발생 위치를 찾아서 st_pos에 저장한다.
en_pos = html_doc.find(en_str)  # en_str이 html_doc에서 처음으로 나타나는 위치를 찾는다.  
p_doc = html_doc[st_pos:en_pos]  # html_doc에서 st_pos부터 en_pos까지의 부분 문자열을 p_doc에 저장한다.
soup_p = BeautifulSoup(p_doc, 'html.parser')  # p_doc를 html.parser로 파싱하여 soup_p에 저장
ranks2 = soup_p.select('p')  # 'p' 태그를 선택하여 ranks2 변수에 저장
print(ranks2[1])
print(ranks2[3])