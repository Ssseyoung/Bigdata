'''
택시 기사가 오늘 받을 손님 수를 N 변수에 입력하고 N번 만큼 손님의 요금을 
input 받아서 리스트에 저장한 후 오늘의 총 수입을 출력하시오
'''

N = int(input('오늘의 손님수: '))
# print(N)
i = 1
total = 0

while(True):
    fee = int(input(str(i)+'번째 손님요금: '))
    total += fee
    i += 1
    if i > N:
        break
    
print('총수입은: ', total)