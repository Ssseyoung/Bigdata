import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
    'aaaa' : [1,1],
    'bbbb' : [2,2],
    'cccc' : [3,3],
    }
)
# 컬럼명 변경 rename
df.index = ['A', 'B']
df.columns = ['한국', '중국', '일본']
df2 = pd.DataFrame({
    '한국' : [30,30], '중국' : [50,50], '일본' : [100,100]
})
# print(df)
# print(df2)
# print(df.loc['A']) 
# print(df.iloc[0])
print(df.append(df2, ignore_index=True))