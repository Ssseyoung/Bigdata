import numpy as np
import pandas as pd

# 1. 불러오기
csv_file = 'data/movies.csv'
df = pd.read_csv(csv_file, encoding='utf-8')
# movieId, title, genres
# 인덱스 번호
# print(df)

# 2. 장르 종류 가져오기
# print(df['genres'].count())
# print(df.loc[10,:'genres'])

genres = [] # 장르의 정보를 저장
for gen in df['genres']:  # df의 'genres' 열을 gen으로 순회하면서 반복 
    # print(type(gen))  # 문자로 되어있는지 확인
    genres.extend(gen.split('|'))  # gen을 '|'로 분리하여 genres 리스트에 추가

# print(genres)
# print(len(genres))

# 3. 장르들이 중복됨 - 중복제거
uni_genres = pd.unique(genres)
# print(len(pd.unique(genres)))

# 4. 장르별 영화 갯수
zero_result = np.zeros(len(uni_genres)) # uni_genres의 길이만큼 0으로 채워진 배열 생성
result = pd.DataFrame(zero_result, index=uni_genres, columns=['갯수'])
# print(result)
# for gen in df['genres'] : 이거 대신 아래 코드가 된 이유?
for g in genres:    # 장르를 | 로 분리해서 다 저장한 목록
    result.loc[g] += 1
# print(result)

# 5. 제목에서 '연도'정보를 추출해서 새로운 컬럼을 만드시오
# print(df['title'].str.extract(r'(\d{4})'))
# print(df['title'].str[-5:-1])

years = []
for title in df['title']:
    years.append(title[-5:-1])

df_years = pd.DataFrame(years, columns=['mov_year'])
df = pd.concat([df, df_years], axis=1)
print(df)