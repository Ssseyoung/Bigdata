# 1-N 까지의 합을 구해서 출력하는 함수

def sum(n):
    total=0
    for i in range(1, n+1):     # n+1 은 0부터 시작하기 때문에
        total = total + i
    # print('합계는 : ', total)
    return total
    
N=100
# sum(N)
result = sum(N) 
print('합계는 : ', result)
    
    