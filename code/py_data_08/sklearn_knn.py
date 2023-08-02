import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split  
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

iris_data = iris.data   # numpy data
col_name = iris.feature_names   # columns
    # iris 데이터셋의 특성 이름을 가져옴
       
df_iris = pd.DataFrame(data=iris_data, columns=col_name)  
    # iris_data와 col_name을 사용하여 DataFrame 생성
print(len(df_iris))
# print(df_iris)
  
# 데이터를 가공 = 데이터 처리 - 비정형데이터

# 지도학습 = 데이터 + 답(타겟)
# print(iris.target)  # 150개의 훈련 및 테스트 데이터

# 학습하기 위해 훈련데이터 + 테스트데이터
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)  
    # iris 데이터셋에서 'data'와 'target'을 train과 test로 분할, 랜덤 시드는 0으로 설정
    # x는 훈련용의 답, y는 테스트용의 답

print('x_train 개수 :', x_train.shape)
print('y_train 개수 :', y_train.shape)

print('x_test 개수 :', x_test.shape)
print('y_test 개수 :', y_test.shape)
    # train:75%(112개), test:25%(38개)

super_knn = KNeighborsClassifier(n_neighbors=9)  
    # KNN 분류기 객체 생성, 이웃의 수는 9로 설정  # 홀수를 줌(짝수는 대칭이 되어 가운데 기준이 없음)
super_knn.fit(x_train, y_train)  
    # x_train과 y_train 데이터를 사용하여 super_knn 모델을 학습시킴

accurency = super_knn.score(x_test, y_test)  
    # x_test와 y_test를 사용하여 super_knn 모델의 정확도를 계산하여 accurency 변수에 저장한다.
print('테스트의 정확도 :', accurency)

# 예측하기
z_new = [[6.0, 2.5, 4.6, 0.5]]    # iris 중에 무슨 품종인지 예측하기
np_z_new = np.array(z_new)
print('새로운 데이터 :', np_z_new)
pre_result = super_knn.predict(np_z_new)
print(iris['target_names'])
print('예측값은 : ', iris['target_names'][pre_result])
