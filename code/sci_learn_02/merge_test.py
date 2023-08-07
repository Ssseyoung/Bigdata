# 직원 정보, 부서정보
# 공통된 컬럼(dept_id)으로 교집합을 구하시오

# 공통된 컬럼(emp_id,mng_id)
# 부서정보 총무 1400으로 변경하고 교집합을 구하시오

import pandas as pd

df_emp = pd.read_csv('data/emp_data2.csv')
df_emp['dept_id'] = df_emp['dept_id'].astype(float)  # 'dept_id' 열의 데이터 타입을 float으로 변환

df_dep = pd.read_csv('data/dept_data2.csv')
df_dep['dept_id'] = df_dep['dept_id'].astype(float)  # 'dept_id' 열의 데이터 타입을 float으로 변환

df_result = pd.merge(df_emp, df_dep, on='dept_id', how='left')  
# df_emp와 df_dep를 dept_id를 기준으로 왼쪽 조인하여 df_result에 저장한다. 
print(df_result)