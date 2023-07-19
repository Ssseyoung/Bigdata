html_doc = '''
    <div class="clock wall">
        <h2>벽시계1</h2>
        <h2>벽시계1</h2>
    </div>

    <div class="clock hand">
        <h2>손목시계1</h2>
        <h2>손목시계1</h2>
    </div>
'''

from bs4 import BeautifulSoup   
# 호출

soup = BeautifulSoup(html_doc, 'html.parser')   
# 생성

print(soup.prettify())  
# soup 객체를 예쁘게 출력

clock = soup.find_all('div', class_='clock')  
# 'div' 태그 중 class가 'clock'인 모든 요소를 찾아서 clock 변수에 할당

clock_hand = soup.find_all('div', class_='clock hand')  
# 'div' 태그 중 class가 'clock hand'인 모든 요소를 찾아서 clock_hand 변수에 할당

print(clock)  
# clock 변수 출력

print(clock_hand) 
# clock_hand 변수 출력

