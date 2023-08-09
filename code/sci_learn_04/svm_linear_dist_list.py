# x점들과 직선의 거리 -> 최소
# w점들과 직선의 거리 -> 최소

import math
import numpy as np

x = [[2, 3],[4, 5]]    # 0번째, 1번째
w = [[7, 1],[10,2]]
nx = np.array(x)
print(nx)
nw = np.array(w)
print(nw)

a1 = 1
b1 = 2
c1 = 1
nx[:, 0] *= a1  # nx의 모든 행의 첫 번째 열에 a1을 곱한다
nx[:, 1] *= b1 
print(nx)
nw[:, 0] *= a1  
nw[:, 1] *= b1 
print(nx)

sum_abs_x = np.abs(np.sum(nx, axis=1) + c1)  
    # nx 행렬의 각 행의 합에 c1을 더하고, 절댓값을 취한 값
print(sum_abs_x)
sum_abs_w = np.abs(np.sum(nx, axis=1) + c1)
print(sum_abs_w)

dis_x = sum_abs_x / math.sqrt(a1**2 + b1**2)  # 거리 계산
print(dis_x)
dis_w = sum_abs_w / math.sqrt(a1**2 + b1**2)
print(dis_w)

# 거리 리스트에서 최소값
min_dis_x = np.min(dis_x)
print(min_dis_x)
min_dis_w = np.min(dis_w)
print(min_dis_w)