# 제목: 함수 만들기 예제
# 개요: 파이썬 문법을 연습 후 -> 주제로 프로그램 만들기 연습
# (예시: 크롤링, 데이터분석, 시각화, 알고리즘, 간단한게임, )
# 주제: 심플게임: 숫자맞추기
# 문제1 함수구현: 1~100까지의 랜덤한 숫자를 발생하는 함수
# 풀이1 check1.py
import random
def generate_random_number():
    return random.randint(1, 99)

# 문제2 함수구현: 랜덤한 숫자를 맞추는 함수
#     숫자를 입력을 했는데
#     맞는 경우
#         함수가 끝나면서 결과를 리턴
#     틀리는 경우
#         다시 입력을 받아서 확인
#         랜덤숫자 55 > 40 : 숫자를 더 올려라 (UP)
#         랜덤숫자 55 < 90 : 숫자를 더 내려라 (DOWN)
# 풀이2 check2.py
def compare_numbers(random_num):

    input_str = input('1~99사이의 숫자를 입력하시오: ')
    input_number = int(input_str)
    result = 0
    if random_num > input_number:
        print('더 큰수를 입력하시오 (UP)')
        result = 0
    elif random_num < input_number:
        print('더 작은수를 입력하시오 (DOWN)')
        result = -1
    else:
        return 1

import check1 as ck1
import check2 as ck2

def main():

    random_number = ck1.generate_random_number()
    count = 0

    # print(random_number)
    while True :
        count += 1
        if ck2.compare_numbers(random_number) == 1:
            print(f'맞춘 랜덤숫자는 {random_number}이고 {count} 시도했습니다')
            break


if __name__ == "__main__":
    main()

# 결과물: 입력횟수: 5번 정답: 55 출력하고 게임 OVER        

# 주제: 야구 숫자 게임
# 문제3 중복되지 않는 2자리 숫자 만드는 함수 generate_num()
# (예시) 34,78(ok) 77,99(x)
# 풀이3
import random

def generate_numbers():
    numbers = []
    i = 0
    new_number = 0
    while i < 2:
        new_number = random.randint(0, 9)
        if i==0 and new_number==0:
            new_number = 1
        if new_number not in numbers:
            numbers.append(new_number)
            i += 1
    print("중복되지 않도록 0~9 사이의 2개를 랜덤한 순서로 뽑음 \n")
    return numbers

# 문제4 숫자 판별하는 함수 check_num()
# (예시) 34(랜덤숫자) - 입력 18 하고 비교 후 - 없음
# (예시) 34(랜덤숫자) - 입력 32 하고 비교 후 - 1S
# (예시) 34(랜덤숫자) - 입력 35 하고 비교 후 - 1S
# (예시) 34(랜덤숫자) - 입력 43 하고 비교 후 - 2B
# (예시) 34(랜덤숫자) - 입력 34 하고 비교 후 - 2S
def check_num(guess, solution):
    strike_count = 0
    ball_count = 0
    i = 0

    while i < len(guess):
        if guess[i] == solution[i]:
            strike_count += 1
            i += 1
        elif guess[i] in solution:
            ball_count += 1
            i += 1
        else:
            i += 1

    return strike_count, ball_count

# 문제5 문제4번 함수를 반복한 후 정답이 나오면
# 점수 출력 함수 get_score()
# 몇번 시도했냐? 정답은 뭐냐? 출력 마무리
# 풀이5
# 여기서부터 게임 시작!
# 메인 부분
import check3 as ck3
import check4 as ck4
ANSWER = ck3.generate_numbers()
tries = 0

def take_guess():
    print("숫자 2개를 하나씩 차례대로 입력하세요.")
    i = 0
    new_guess = []
    while i < 2:
        gue_number = int(input("{}번째 숫자를 입력하세요: ".format(i + 1)))
        if gue_number > 9:
            print("범위를 벗어난 숫자입니다 다시 입력하세요.")
            continue
        if gue_number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요. ")
        else:
            new_guess.append(gue_number)
            i += 1

    return new_guess

while 1:
    GUESS = take_guess()
    strike, ball = ck4.check_num(GUESS, ANSWER)
    print("{}S {}B ".format(strike, ball))

    if strike == 2:
        tries += 1
        break
    else:
        tries += 1

print("당신은 {}번 만에 숫자 2개의 값과 위치를 모두 맞추셨습니다.".format(tries))