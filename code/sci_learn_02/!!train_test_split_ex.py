# fish 데이터를 읽어오기
# 160개

# x_train = [[무게, 길이, 높이, 너비]] 80% 랜덤하게 가져오기
# x_test  = [[무게, 길이, 높이, 너비]] 20% 랜덤하게 가져오기

# y_target = [[이름]] 물고기 이름
# y_test   = [[이름]] 물고기 이름

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  
from sklearn.neighbors import KNeighborsClassifier  

fish = pd.read_csv('data/Fish.csv', encoding='cp949')
# print(fish)

df = pd.DataFrame(fish)
print(len(df))

x_train, x_test, y_train, y_test = train_test_split(
    df[['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']], df[['癤풱pecies']], random_state=0)  
    # iris 데이터셋에서 'data'와 'target'을 train과 test로 분할, 랜덤 시드는 0으로 설정
    
print('x_train 개수 :', x_train.shape)
print('y_train 개수 :', y_train.shape)

print('x_test 개수 :', x_test.shape)
print('y_test 개수 :', y_test.shape)

super_knn = KNeighborsClassifier(n_neighbors=9)  
    # KNN 분류기 객체 생성, 이웃의 수는 9로 설정  # 홀수를 줌(짝수는 대칭이 되어 가운데 기준이 없음)
super_knn.fit(x_train, y_train)  
    # x_train과 y_train 데이터를 사용하여 super_knn 모델을 학습시킴

accurency = super_knn.score(x_test, y_test)  
    # x_test와 y_test를 사용하여 super_knn 모델의 정확도를 계산하여 accurency 변수에 저장한다.
print('테스트의 정확도 :', accurency)

# 예측하기
z_new = [[230,21.9,23.5,29,10.78,4.01]]
np_z_new = np.array(z_new)
print('새로운 데이터 :', np_z_new)
pre_result = super_knn.predict(np_z_new)
print(df['癤풱pecies'])
print('예측값은 : ', df['癤풱pecies'][pre_result])