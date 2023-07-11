# 점수리스트 배열
score_list=[80, 75, 96]
print(score_list)

# 점수를 입력해서 점수리스트에 저장하는 함수
sc1 = input("점수는 : ")
sc2 = input("점수는 : ")
sc3 = input("점수는 : ")

sc1 = int(sc1)
sc2 = int(sc2)
sc3 = int(sc3)

read_score = [sc1, sc2, sc3]
print(read_score)

# 평균을 구하는 함수
def read_score(sc1, sc2, sc3):
    avg = 0
    avg = (sc1 + sc2 + sc3)/3
    avg = round(avg, 1)
    return avg

result = read_score(sc1, sc2, sc3)
print('평균은 : ', result)

# 최대값을 구하는 함수
print('최대값 : {}'.format( max(sc1, sc2, sc3) ))
    
    
    