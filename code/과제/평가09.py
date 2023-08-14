import requests
from bs4 import BeautifulSoup

URL = "https://autobuff.co.kr/1962/"

# HTTP GET 요청을 보내고 응답을 받음
response = requests.get(URL)

# BeautifulSoup을 이용해서 HTML 파싱
soup = BeautifulSoup(response.content, 'html.parser')

# 웹페이지에서 2022년 자동차 판매 순위가 있는 요소를 찾음
table = soup.find('class', {'wp-block-heading'})  
print(table)

# 순위 1~5위까지의 자동차 이름을 표시하기 위한 리스트 초기화
# top_cars = []

# # 순위 1~5위까지의 자동차 이름을 추출하여 리스트에 저장
# for row in table.tbody.find_all('tr'):
#     rank = row.find('td', {'class': 'rank'}).text.strip()
#     name = row.find('td', {'class': 'title'}).text.strip()
#     if 1 <= int(rank) <= 5:
#         top_cars.append((rank, name))

# 가져온 데이터를 출력
# print("2022년 자동차 판매 순위 1~5위:\n")
# for rank, name in top_cars[::-1]:
#     print(rank, "위:", name)