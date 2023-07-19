html_doc = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <div class="wrapper">
        <div id="header">
            <header>
                <h2>My Blog</h2>
                
                <ul id="menu">

                    <li class="subject">HOME</li>
                    <li class="subject">INTRO</li>
                    <li class="subject">SERVICE</li>
                    <li class="subject">NOTICE</li>
                    <li class="subject">CONTACT</li>

                </ul>
            </header>
        </div>
    </div>
</body>
</html>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')  # html_doc을 파싱하여 BeautifulSoup 객체 생성
print(soup.prettify())  # BeautifulSoup 객체를 예쁘게 출력  # soup 객체의 prettify() 메소드를 호출하여 HTML 코드를 깔끔하게 출력합니다.

ul_tag = soup.find('ul', id='menu')  # 'menu' id를 가진 ul 태그를 찾음
li_tags = ul_tag.find_all('li', class_='subject')  # 'subject' 클래스를 가진 모든 li 태그를 찾음
print(li_tags)  # li 태그들을 출력