# 파이썬에서 정규표현식을 활용 : re 모듈
import re

import re  # re 모듈을 임포트합니다.

text = 'python is good for data'  # 변수 text에 문자열 'python is good for data'를 할당합니다.
mat = re.search('python', text)  # re.search 함수를 사용하여 'python'이라는 패턴을 찾습니다.
result = mat.group()  # 찾은 패턴을 result 변수에 할당합니다.
print(result)  # result를 출력합니다.