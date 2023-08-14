# 1~1000 사이의 정수 중에 
# 홀수인 값만 모두 더하여 출력하시오

sum = 0
for i in range(1,1001,2):   # 1부터 1000까지의 홀수를 반복
    sum += i               # i를 sum에 누적
print(sum)