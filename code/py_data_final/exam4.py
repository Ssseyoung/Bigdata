# 세종시
# 2012년 ~ 2017년까지
# 30대 인구수(조치원읍)

import pandas as pd

xlsx_filename = 'data/201212_201712_연령별인구현황_연간.xlsx'
a = pd.read_excel(xlsx_filename)

df = pd.DataFrame(a)
# print(df)

# 컬럼이름 확인 또는 갯수
# print('컬럼갯수: ', len(df.columns))

# print(df.iloc[4,4]) # 2012
# print(df.iloc[4,13]) # 2013
# print(df.iloc[4,22]) # 2014
# print(df.iloc[4,31]) # 2015
# print(df.iloc[4,40]) # 2016
# print(df.iloc[4,49]) # 2017

# 4행의 4번째 열부터 데이터프레임의 열 길이까지 9씩 증가하는 범위에서 데이터를 출력한다.
print(df.iloc[4,range(4, len(df.columns), 9)])