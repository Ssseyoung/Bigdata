import pandas as pd
import numpy as np

emp = {
    'emp_id' : [1000, 1100, 1200, 1300, 1400],
    'name' : ['아이유', '카리나', '권나라', '채수빈', '장원영'],
    'salary' : [25000, 30000, 40000, 30000, 30000],
    'dept_id' : [2,1,2,2,3]
}

df = pd.DataFrame(emp)
# print(df)

# mng_id 추가
df['mng_id'] = [1300, 1100, 1300, 1300, 1400]

# df['mng_id'] = pd.np.where(df['dept_id']==2, 1300,  # dept_id가 2인 경우 mng_id에 1300을 할당
#                            pd.np.where(df['dept_id']==1, 1100, 1400))  # dept_id가 1인 경우 mng_id에 1100을 할당, 그 외의 경우에는 mng_id에 1400을 할당

# position : True(시니어), False(쥬니어)
# 급여가 40000이상 : True
df['position'] = df['salary'] >= 40000
# print(df)

# drop() 함수
df = df.drop('mng_id', axis=1)
print(df)