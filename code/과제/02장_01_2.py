def read_score():
    while True:
        score = input("점수를 입력하세요 (종료: end): ")  
        if score == 'end': 
            break
        score_list.append(float(score)) 

def average(scores):
    return sum(scores) / len(scores)  

def max_score(scores):
    return max(scores) 

# 점수 리스트 배열
score_list = []

# 점수를 입력해서 점수 리스트에 저장
read_score()

# 평균 구하기 및 출력
average_score = average(score_list)  # score_list의 평균을 계산하여 average_score 변수에 저장
print("평균 점수:", average_score)  # 평균 점수를 출력

# 최대값 구하기 및 출력
max_value = max_score(score_list)  # score_list에서 최대값을 구하여 max_value 변수에 저장
print("최대 점수:", max_value)  # 최대 점수를 출력