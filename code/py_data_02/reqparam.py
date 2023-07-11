import requests

URL = 'https://serieson.naver.com/v3/movie'

param = {'query' : '스페셜'}
response = requests.get(URL, params=param)

if response.status_code==200:
    print('성공')
else:
    print('실패')