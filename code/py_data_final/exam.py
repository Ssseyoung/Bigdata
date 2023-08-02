# https://autobuff.co.kr/1962/
# 자동차 판매순위 사이트에 있는 차량 10개의 이미지를 다운로드
# bs를 사용하여 분석

# import urllib.request # http 요청 객체
# import requests # 외부모듈

# img_src = 'https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/%EC%82%AC%EC%A7%844_%ED%98%84%EB%8C%80%EC%B0%A8_%EC%97%94%ED%8A%B8%EB%A6%AC_SUV_%E2%80%98%EC%BA%90%EC%8A%A4%ED%8D%BC_%EC%B6%9C%EC%8B%9C.jpg?resize=1024%2C682&ssl=1'
# save_path = 'images/'
# save_file = 'img01.jpg'
# urllib.request.urlretrieve(img_src, save_path+save_file)

# img_src = 'https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/%ED%8C%B0%EB%A6%AC%EC%84%B8%EC%9D%B4%EB%93%9C1.jpg?resize=1024%2C682&ssl=1'
# save_path = 'images/'
# save_file = 'img02.jpg'
# urllib.request.urlretrieve(img_src, save_path+save_file)

# img_src = 'https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/444.jpg?resize=1024%2C682&ssl=1'
# save_path = 'images/'
# save_file = 'img03.jpg'
# urllib.request.urlretrieve(img_src, save_path+save_file)

# img_src = 'https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/%EC%8C%8D%EC%9A%A9%EC%B0%A8_%ED%86%A0%EB%A0%88%EC%8A%A4.jpg?resize=1024%2C728&ssl=1'
# save_path = 'images/'
# save_file = 'img04.jpg'
# urllib.request.urlretrieve(img_src, save_path+save_file)

# img_src = 'https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/143414312.jpg?resize=1024%2C682&ssl=1'
# save_path = 'images/'
# save_file = 'img05.jpg'
# urllib.request.urlretrieve(img_src, save_path+save_file)

# img_src = 'https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/321123.jpg?resize=1024%2C683&ssl=1'
# save_path = 'images/'
# save_file = 'img06.jpg'
# urllib.request.urlretrieve(img_src, save_path+save_file)

# img_src = 'https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/444-1.jpg?resize=1024%2C683&ssl=1'
# save_path = 'images/'
# save_file = 'img07.jpg'
# urllib.request.urlretrieve(img_src, save_path+save_file)

# img_src = 'https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/222.jpg?resize=1024%2C465&ssl=1'
# save_path = 'images/'
# save_file = 'img08.jpg'
# urllib.request.urlretrieve(img_src, save_path+save_file)

# img_src = 'https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/%EB%B4%89%EA%B3%A0_3_ev.jpg?resize=1024%2C682&ssl=1'
# save_path = 'images/'
# save_file = 'img09.jpg'
# urllib.request.urlretrieve(img_src, save_path+save_file)

# img_src = 'https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/%ED%8F%AC%ED%84%B0_2_%EC%9D%BC%EB%A0%89%ED%8A%B8%EB%A6%AD.jpg?resize=1024%2C682&ssl=1'
# save_path = 'images/'
# save_file = 'img10.jpg'
# urllib.request.urlretrieve(img_src, save_path+save_file)


# Import requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup

# Define the URL of the website
url = "https://autobuff.co.kr/1962/"

# Get the HTML content of the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all the <img> tags that have the class "wp-block-image size-large"
# images = soup.find_all("img", class_=p)
images = soup.find_all("figure" ,class_='wp-block-image size-large')
# Loop through the first 10 images and print their source attribute

for image in images[:10]:
     print(image.img["src"])

