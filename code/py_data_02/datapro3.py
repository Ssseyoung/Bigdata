
text = '2021-12-25, 김건우, 지금 업무중...'
print(text)  # text 변수 출력
text_strip = text.strip()  # 문자열 앞뒤 공백 제거
print(text_strip)  # 앞뒤 공백이 제거된 문자열 출력
text_strip2 = text_strip.replace(' ','')  # 공백 제거
print(text_strip2)  # 공백이 제거된 문자열 출력
print(text_strip2.replace('.',''))  # text_strip2에서 '.'을 제거한 결과를 출력한다.

text2 = '   happy.new-year, myfriend   '  # 초기 문자열을 정의한다.
temp = text2.strip()  # 문자열의 양쪽 공백을 제거한다.
temp2 = temp.replace(' ','')  # 문자열 내의 공백을 제거한다.
temp3 = temp2.replace('-',' ')  # 문자열 내의 '-'를 공백으로 대체한다.
temp4 = temp3.replace('.',' ')  # 문자열 내의 '.'를 공백으로 대체한다.
print(temp4)  # 결과 문자열을 출력한다.

import re  # 정규표현식 모듈을 import
text3 = '    today, weather    '  # 공백이 포함된 문자열을 변수에 할당
result = re.sub(r'\s+', '', text3)  # 정규표현식을 사용하여 공백을 제거한 결과를 변수에 할당
print(result)  # 결과 출력

