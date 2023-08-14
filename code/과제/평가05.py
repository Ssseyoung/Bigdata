st_name = ['송지우', '심현준', '윤호민']
st_score = [93, 78, 89]

for i in range(len(st_name)):   # 학생 수 만큼 반복
    if st_score[i] >= 90:
        grade = 'A'
    elif st_score[i] >= 80:
        grade = 'B'
    elif st_score[i] >= 70:
        grade = 'C'
    elif st_score[i] >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(st_name[i], '학생의 학점은', grade, '입니다.')