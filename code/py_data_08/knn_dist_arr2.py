import numpy as np

fish_length = [25.4, 26.3, 29, 9.8, 10.3, 10.7]
fish_weight = [242.0, 290.0, 340.0, 6.8, 7.0, 7.8]
fish_answer = [0, 0, 0, 1, 1, 1]
new_fish = [20.0, 150]

# 거리를 비교해서 0이면 잉어예측, 1이면 송사리예측으로 예측하시오

# 훈련데이터를 np자료형 변환
# fish_length와 fish_weight를 numpy 배열로 변환
np_f_length = np.array(fish_length)
np_f_weight = np.array(fish_weight)

# 새로운 물고기와 기존 물고기들의 길이 차이의 제곱과 무게 차이의 제곱을 계산하여 더함
temp = (np_f_length - new_fish[0])**2 + (np_f_weight - new_fish[1])**2

# temp의 제곱근을 계산하여 결과를 얻음
result = np.sqrt(temp)

# 결과 출력
print(result)