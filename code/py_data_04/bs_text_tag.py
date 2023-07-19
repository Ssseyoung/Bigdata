text = '''
        <li class="item">
            <a class="item_link" href="www.naver.com">
                <span>네이버</span>
            </a>
        </li>  
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(text, 'html.parser')
# print(soup.prettify())
result = soup.find('span')
print(result)
print('텍스트 내용 :', result.string)

print('텍스트 내용2 :', soup.get_text().strip())
