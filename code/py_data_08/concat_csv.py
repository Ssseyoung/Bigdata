import pandas as pd

# 방법 1
data1 = pd.read_csv('data/concat_1.csv', encoding='utf-8')
data2 = pd.read_csv('data/concat_2.csv', encoding='utf-8')
data3 = pd.read_csv('data/concat_3.csv', encoding='utf-8')

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# print(pd.concat([df1, df2, df3], ignore_index=True))

# 방법 2
df_all = pd.DataFrame()
for num in range(1,4):
    path = 'data/concat_%d.csv' %num  # 파일명이 숫자 순서대로 되어있는 경우
    df = pd.read_csv(path)
    df_all = pd.concat([df_all, df], ignore_index=True)
    
print(df_all)
