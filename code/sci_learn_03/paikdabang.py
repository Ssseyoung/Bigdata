import requests
from bs4 import BeautifulSoup

# 빽다방 매장 검색 URL
url = "https://paikdabang.com/store/map"

# 검색할 구 리스트
districts = ['강남구', '종로구', '마포구']

# HTML 파싱
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for district in districts:
    # 해당 구의 매장 정보 가져오기
    stores = soup.select(f'.store_detail[data-area={district}]')

    # 결과 출력
    store_count = len(stores)
    print(f"{district}: {store_count}개 매장")