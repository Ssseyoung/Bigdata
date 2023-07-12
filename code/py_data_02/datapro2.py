text = '<div><h2>오늘의 요리를 소개합니다</h2></div>'

start = text.find('오늘')  # '오늘'이 처음으로 나오는 위치를 찾아서 start 변수에 저장
text_temp = text[start:start+6]  # start 위치부터 6글자를 잘라서 text_temp 변수에 저장
text_strip = text_temp.strip()  # 문자열 앞뒤의 공백 제거
print(text_temp)  # text_temp 변수의 값을 출력

if text_temp == '오늘의 요리':  # text_temp 변수가 '오늘의 요리'와 같은지 비교
    print('같은 문자열')  # '같은 문자열'을 출력
else:
    print('다른 문자열')  # '다른 문자열'을 출력