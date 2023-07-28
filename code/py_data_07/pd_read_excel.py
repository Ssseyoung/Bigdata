import pandas as pd

file_path = 'data/products.xlsx'

df = pd.read_excel(file_path)

# print(df)

total_sale = df['판매가'].sum()
# print(total_sale)

# 행 데이터 합을 구하기 전에 분류번호, 판매가, 원가 : 3컬럼만 선택
df2 = df[['분류번호', '판매가', '원가']]    # 여러 컬럼은 대괄호 2개
# print(df2)
total_sale2 = df2['판매가'].sum()
total_sale2m = df2['판매가'].mean()
total_sale2max = df2['판매가'].max()
total_sale2amax = df2['판매가'].argmax()

# print('제품판매가의 총합 : ', total_sale2)
# print('제품판매가의 평균 : ', total_sale2m)
# print('제품판매가의 최대값 : ', total_sale2max)
# print('제품판매가의 최대값 위치 : ', total_sale2amax)

total_sale3 = df2.loc[0:2].sum(axis=1) # 1 행으로 합
# print('행별로 총합 : ', total_sale3)

# 판매가 - 원가 계산해서 마진가 컬럼에 추가
df['마진가'] = df['판매가'] - df['원가']
# print(df)
index = df['마진가'].argmax()
# print(df.loc[index])

# 원가 가장 최소값인 제품명, 마진가를 출력
id_min = df['원가'].argmin()
# print(df.loc[id_min, ['이름', '마진가']])

# 분류번호 20번이 제품 중 판매가가 제일 비싼 제품의 번류번호, 이름, 판매가
print(df.loc[df[df['분류번호']==20]['판매가'].argmax(),['분류번호', '이름', '판매가']])

'''
# df 데이터프레임에서 '분류번호' 열이 20인 행을 찾고, 해당 행의 '판매가' 열의 최댓값을 가지는 행의 인덱스를 반환한다.
max_index = df[df['분류번호'] == 20]['판매가'].argmax()
# max_index에 해당하는 행에서 '분류번호', '이름', '판매가' 열의 값을 출력한다.
print(df.loc[max_index, ['분류번호', '이름', '판매가']])
'''

# 분류번호 중복제거
narr_code = df['분류번호'].unique()
# print(df_code)  # numpy 행렬값
# print(type(df_code))
df_code = pd.DataFrame(narr_code, columns=['분류코드'])
print(df_code)