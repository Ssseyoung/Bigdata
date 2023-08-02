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