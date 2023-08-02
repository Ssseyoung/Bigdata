import pandas as pd
import numpy as np

def count_miss(vec) :
    null_vec = pd.isnull(vec)
    null_cnt = np.sum(null_vec)
    return null_cnt

data = [
    [1, None, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [None, 1, 1, 1, None]
]
col_name = ['AA', 'BB', 'CC']

# 데이터프레임 만들고 누락된 값의 갯수를 출력하시오
df = pd.DataFrame(data, col_name)
print(df)
total = df.apply(count_miss)
# print(total)
