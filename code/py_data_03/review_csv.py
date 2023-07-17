import csv
import os

if os.path.exists('data/scores.csv'):  # 'data/scores.csv' 파일이 존재하는지 확인
    fc = open('data/scores.csv', 'r', encoding='utf-8')  # 'data/scores.csv' 파일을 읽기 모드로 열기
    scores = csv.reader(fc)  # 파일 객체를 csv.reader로 읽기
    next(scores)  # 첫 번째 행(헤더)을 건너뛰기
    result = []  # 결과를 저장할 빈 리스트 생성
    for s in scores:  # scores에서 각 행을 순회하며
        temp = s[2].strip().split('|')  # s 리스트의 세 번째 요소를 가져와서 양쪽 공백을 제거하고 '|'를 기준으로 분리하여 temp 리스트에 저장한다.
        temp2 = [int(num) for num in temp]  # temp 리스트의 각 요소를 정수로 변환하여 temp2 리스트에 저장
        # print(sum(temp2))
        result.append(sum(temp2))  # temp2 리스트의 합을 구하여 result 리스트에 추가한다.
        
        # result.extend(s[2].strip().split('|'))     # strip 공백 제거
else:
    print('없음')
    
# print(list(set(result)))

print(result)