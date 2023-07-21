'''
다음 샘플 json 데이터를 requests 객체를 사용하여 요청한 후 
딕셔너리 자료형으로 변환하시오 
데이터 안에는 title 속성 정보가 있는데 이 속성 정보만 뽑아서 출력하시오

주소: https://jsonplaceholder.typicode.com/posts
'''

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

title = [post["title"] for post in data]

print(title)
    
    