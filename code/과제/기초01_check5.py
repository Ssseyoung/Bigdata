'''
숫자로만 구성된 리스트 자료형을 받아서 짝수값만 반환하는 even_check_list 함수를 구현하여 
샘플 데이터는 [4,3,5,6,9,5,3,2,6,8] 이며 실행해서 함수의 결과를 반환한 후 출력하시오
'''

def even_check_list(zz):
    even_zz = [num for num in zz if num%2 == 0]
    return even_zz

sample_data = [4,3,5,6,9,5,3,2,6,8]
result = even_check_list(sample_data)
print(result)