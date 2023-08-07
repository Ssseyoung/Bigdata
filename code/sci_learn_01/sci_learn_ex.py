from sklearn.datasets import load_iris
import pandas as pd

iris_origin = load_iris()

iris_data = iris_origin.data
# print(iris_data)

iris_label = iris_origin.target  # iris_origin의 target 값을 iris_label 변수에 저장
# print(iris_label)

df_iris = pd.DataFrame(iris_data, columns=iris_origin.feature_names)  
# iris_data를 이용하여 DataFrame 생성, 열 이름은 iris_origin의 feature_names 사용
print(df_iris)