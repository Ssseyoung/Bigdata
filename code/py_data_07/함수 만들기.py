'''
    제목 : 함수 만들기 예제
    개요 : 파이썬 문법을 연습 후 -> 주제로 프로그램 만들기 연습
    (예시 : 크롤링, 데이터 분석,  시각화, 알고리즘, 간단한 게임)
    주제 : 심플게임(숫자맞추기)

    문제 1) 함수구현 : 1 ~ 100까지의 랜덤한 숫자를 발생하는 함수
    
    문제 2) 함수구현 : 랜덤한 숫자를 맞추는 함수
        숫자를 입력을 했는데
        
        맞는 경우
            함수가 끝나면서 결과를 리턴
            
        틀리는 경우
            다시 입력을 받아서 확인
            랜덤 숫자 55 > 40 : 숫자를 더 올려라 (UP) 
            랜덤 숫자 55 < 90 : 숫자를 더 내려라 (DOWN) 
            
        결과물 : 
        입력횟수 5번
        정답 : 55
        출력하고 게임 OVER
        
'''

import pandas as pd

target = 55

# 시행횟수를 저장할 변수를 초기화합니다.
count = 0

# 맞추기 위한 범위를 저장할 데이터프레임을 생성합니다.
df = pd.DataFrame({'lower': [1], 'upper': [100]})

# 범위의 중간값을 구하는 함수를 정의합니다.
def get_mid(row):
    return (row['lower'] + row['upper']) // 2

# 범위를 반으로 줄이는 함수를 정의합니다.
def update_range(row, target):
    mid = get_mid(row)
    if target < mid:
        return pd.Series({'lower': row['lower'], 'upper': mid - 1})
    elif target > mid:
        return pd.Series({'lower': mid + 1, 'upper': row['upper']})
    else:
        return pd.Series({'lower': mid, 'upper': mid})

# 범위가 하나의 숫자가 될 때까지 반복합니다.
while df['lower'].iloc[0] != df['upper'].iloc[0]:
    # 시행횟수를 증가시킵니다.
    count += 1
    # 범위를 반으로 줄입니다.
    df = df.apply(update_range, axis=1, args=(target,))

# 최종적으로 맞춘 숫자와 시행횟수를 출력합니다.
print(f"맞춘 숫자: {df['lower'].iloc[0]}")
print(f"시행횟수: {count}")