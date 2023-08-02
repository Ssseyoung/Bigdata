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