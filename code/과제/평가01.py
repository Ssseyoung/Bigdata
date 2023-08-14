# 주사위를 2번 던졌을 때 램던하게 나오는 두 개의 숫자를 더하여 출력하는 코드를 구현하시오

import random

dice1 = random.randint(1, 6)  # 첫 번째 주사위 던지기
dice2 = random.randint(1, 6)  # 두 번째 주사위 던지기

sum_dice = dice1 + dice2     # 두 주사위 더하기

print("주사위1 : ", dice1)
print("주사위2 : ", dice2)
print("두 수의 합은 : ", sum_dice)