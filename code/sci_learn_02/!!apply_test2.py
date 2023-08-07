import pandas as pd
import numpy as np

class_data = [
    [1, 90, 70, 100],
    [2, 80, 60, 90],
    [3, 85, 80, 80],
    [4, 95, 70, 90],
    [5, 75, 90, 100],
]

col = ['class', 'eng', 'fra', 'jpn']

# apply 함수를 사용해서 각반의 총점, 평균
# 방법 1
df = pd.DataFrame(class_data, columns=col)

df[['eng', 'fra', 'jpn']] = df[['eng', 'fra', 'jpn']].apply(pd.to_numeric)  
    # 'eng', 'fra', 'jpn' 열의 데이터를 숫자형으로 변환
df['total'] = df['eng'] + df['fra'] + df['jpn']  
    # 'eng', 'fra', 'jpn' 열의 합을 계산하여 'total' 열에 저장
df['avg'] = df[['eng', 'fra', 'jpn']].mean(axis=1) 
    # 'eng', 'fra', 'jpn' 열의 평균을 계산하여 'avg' 열에 저장
print(df)

# 방법 2


# apply 함수를 사용해서 각과목의 총점
# 방법 1
df[['eng', 'fra', 'jpn']] = df[['eng', 'fra', 'jpn']].apply(pd.to_numeric)
print(df.loc[:, 'eng':'jpn'].sum())
    # 'eng'부터 'jpn'까지의 열을 선택하여 합을 계산한다.