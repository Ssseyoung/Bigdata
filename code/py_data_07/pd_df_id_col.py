# 데이터프레임을 만들거나 가져오면
# 다뤄서 처리하려면 index, columns
import pandas as pd

df = pd.DataFrame(
    {'AAA' : ['아이유', '뉴진스', '카리나'],
     'BBB' : [1, 2, 3],
     'CCC' : [100, 200, 300]}
)
# print(df)
# print(df.columns)
# print(df.index)

# 가져오기
b_col = df['BBB']  # df의 'BBB' 열을 b_col 변수에 할당
df['BBB'] = [2,4,6]  # df의 'BBB' 열을 [2,4,6]으로 변경
df['BBB'] = [[1,2],[2,4],[3,6]]  # df의 'BBB' 열을 [[1,2],[2,4],[3,6]]으로 변경
print(df)