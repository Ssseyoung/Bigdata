# 이름의 길이가 같은 꽃들을 분리하여 출력하시오
word = ['해바라기', '나팔꽃', '장미', '무궁화', '코스모스', 
        '접시꽃', '선인장', '제비꽃', '국화', '에델바이스']

# 이름의 길이를 저장할 리스트 초기화
name_length = [0] * len(word) 

# 각 이름의 길이를 계산해서 리스트에 저장
for i in range(len(word)):
    name_length[i] = len(word[i])

# 중복되지 않게 이름의 길이를 집합(set)으로 추출
unique_length = set(name_length)

# 이름의 길이가 같은 꽃들을 분리하여 출력 
for length in unique_length:
    print(length, "글자인 꽃들:", end=' ')
    for i in range(len(word)):
        if len(word[i]) == length:
            print(word[i], end=' ')
    print()