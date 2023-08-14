#  문자열 str과 정수 n이 주어집니다
#  str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요

s = input("문자열을 입력하세요: ")
n = int(input("반복할 횟수를 입력하세요: "))
result = s * n   
print(result)


s1 = input("문자열을 입력하세요: ")
n = int(input("반복할 횟수를 입력하세요: "))
for i in range(n):
    print(s1)
    if i != n-1:     # 마지막 라인에서는 줄바꿈을 하지 않음
        print()