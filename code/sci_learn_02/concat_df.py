# 예제에서는 데이터프레임을 서로 합치는 방법 소개
import pandas as pd

data1 = {
    'no' : [100, 101, 102, 103],
    'name' : ['IU', 'Karina', 'KwunNara', 'Hani'],
    'salary' : [50000, 40000, 35000, 30000]
}

data2 = {
    '번호' : [104],
    '이름' : ['Kara'],
    '급여' : [15000]  
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# print(df1)
# print(df2)

# df3 = pd.concat([df1, df2], axis=1)
# 같은 열끼리 합치는데 컬럼명이 다르므로 컬럼별로 개별적으로 합쳐진다

# 컬럼명 동일하게 해서 합치면
df2.columns = ['no', 'name', 'salary']
df3 = pd.concat([df1, df2], ignore_index=True)
print(df3)