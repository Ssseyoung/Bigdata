# 데이터프레임의 행데이터를 접근 연습
import numpy as np
import pandas as pd

depart = {
    'depart_id' : [1,2,3,4],
    'depart_name' : ['기획', '영업', '개발', '총무']
}
df = pd.DataFrame(depart)

# 열 추가 mng_id = 1100 1200 1400 NULL
df['mng_id'] = [1100, 1200, 1400, np.NaN]

# 행 추가 5 연구 1500
df.loc[4] = [5, '연구', 1500]

# 총무 mng_id 를 NaN -> 1600 변경
df.loc[3, 'mng_id'] = 1600
# 정수로 변경
df['mng_id'] = df['mng_id'].astype(int)

print(df)