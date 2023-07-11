import requests

# # 버거킹 웹사이트의 이벤트 페이지
# URL = 'https://www.burgerking.co.kr/#/event/0/1'

# response = requests.get(URL)  # 웹사이트 주소에 요청

# # print('응답코드 : ', response.status_code)
# if response.status_code == 200:
#     print(response.text)
# else:
#     print('오류 발생')

URL = 'https://serieson.naver.com/v3/movie'

response = requests.get(URL)

# print('응답코드 : ', response.status_code)
if response.status_code == 200:
    print(response.text)
else:
    print('오류 발생')