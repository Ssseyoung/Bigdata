import numpy as np
import pandas as pd
from matplotlib import font_manager, pyplot as plt, rc
font_path ="C:/Windows/Fonts/MALGUN.TTF" 
font = font_manager.FontProperties(fname=font_path).get_name() 
rc('font', family=font)

# 1. 불러오기
xlsx_filename = 'data/치킨집_가공.xlsx'
df = pd.read_excel(xlsx_filename)
# print(df)
# print(len(df))
# print(df.columns)   # 소재지전체주소 사업장명

# 2. 구 정보, 동 정보
goo = []
dong = []
for addr in df['소재지전체주소']:
    goo.append(addr.split()[1])    # 인자값이 없음 : 공백구분
    dong.append(addr.split()[2])
    
# print(dong)
# 구의 갯수(중복제거), 동의 갯수(중복제거)
# print(pd.unique(goo))
# print(pd.unique(dong))
uni_dong = pd.unique(dong)

# 3. 각 동에서 치킨집 몇개씩 있는지
dong_count = np.zeros(len(uni_dong))
result = pd.DataFrame(dong_count, columns=['chk_cnt'], index=uni_dong)

# 4. 동별로 치킨집 갯수 세기

# 4-1.
# for dong in uni_dong:
#     for address in df['소재지전체주소']:
#         if address.find(dong) != -1: 
    
# -1은 문자열에서 특정 문자나 부분 문자열을 찾지 못했을 때 find() 메소드가 반환하는 값입니다.
#  예를 들어, "Hello"라는 문자열에서 "a"를 찾으려고 하면, find() 메소드는 -1을 반환합니다.
#  왜냐하면 "Hello"에는 "a"가 없기 때문입니다.

# 반대로, "Hello"에서 "e"를 찾으려고 하면, find() 메소드는 1을 반환합니다.
# 왜냐하면 "e"는 "Hello"의 두 번째 문자이고, 문자열의 인덱스는 0부터 시작하기 때문입니다.

# 따라서, 코드에서 -1은 주소에 dong이 포함되어 있지 않다는 것을 의미합니다.
# 즉, dong이 df[‘소재지전체주소’]에 있는 주소와 일치하지 않는다는 것입니다.

# 4-2.
# for d in dong:
#     result.loc[d] += 1
# print(result)

# 4-3.
df2 = pd.DataFrame(dong, columns=['dong'])  # 'dong' 데이터를 이용하여 새로운 DataFrame 생성
df = pd.concat([df, df2], axis=1)  # 기존 DataFrame과 새로운 DataFrame을 열 방향으로 합침
df_group_dong = df.groupby('dong')['소재지전체주소'].count()
dong_sorted = list(df_group_dong.index)
# print(df_group_dong)

# 5. 동별로 치킨집의 갯수를 bar 그래프와 비율을 pie 그래프로 나타내시오
x_pos = np.arange(len(dong_count))
y_count = df_group_dong.to_list()

# 2개의 서브 plt
fig = plt.figure()
sub_plt1 = fig.add_subplot(2,1,1)   # 행2 열1 수1
sub_plt2 = fig.add_subplot(2,1,2)   # 행2 열1 수1

plt.subplot(2,1,1)
plt.bar(x_pos, y_count)
plt.xticks(x_pos, dong_sorted)

plt.subplot(2,1,2)
plt.pie(y_count, labels=dong_sorted, autopct='%.1f%%', textprops={'fontsize':6})

plt.show()