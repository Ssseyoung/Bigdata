# 문자열.split() 함수 예제 소개

text = '오늘은 날씨 좋고 미세먼지도 괜찮네요'  # 텍스트 변수에 문자열 할당

words = text.split()  # 공백을 기준으로 문자열을 나누어 리스트로 저장

print(words)  # 리스트 출력

for w in words:  # 리스트의 각 요소에 대해 반복
    print(w)  # 각 요소 출력