'''
2차원 R행(5) C열(5) 로 이루어진 리스트 배열을 선언하고 
1~25까지 값을 대입한 후 저장된 값을 출력하시오
'''

arr = [[0 for _ in range(5)] for _ in range(5)]

count = 1
for r in range(5):
    for c in range(5):
        arr[r][c] = count
        count += 1

for row in arr:
    print(row)