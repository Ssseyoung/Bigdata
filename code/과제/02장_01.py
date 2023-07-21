'''
사용자 함수를 정의하여 리스트 변수에 점수를 저장하고 평균값과 맥스값을 구하는 코드를 작성하시오

#점수리스트배열
score_list = []

#점수를 입력해서 점수리스트에 저장하는 함수
read_score()

#평균을 구하는 함수
#맥스값을 구하는 함수
'''

sc1 = input("점수는 : ")
sc2 = input("점수는 : ")
sc3 = input("점수는 : ")

sc1 = int(sc1)
sc2 = int(sc2)
sc3 = int(sc3)

read_score = [sc1, sc2, sc3]
print(read_score)

def read_score(sc1, sc2, sc3):
    avg = 0
    avg = (sc1 + sc2 + sc3)/3
    avg = round(avg, 1)
    return avg

result = read_score(sc1, sc2, sc3)
print('평균은 :', result)

print('최대값 : {}'.format( max(sc1, sc2, sc3) ))
    
    
    