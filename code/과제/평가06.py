# 숫자와 문자가 섞인 문자열을 입력받아서 숫자가 아닌 문자의 개수를 구하시오

s = input("문자열을 입력하세요: ")
count = 0
for i in s:
    if not i.isdigit():  
        count += 1       

print("숫자가 아닌 문자의 개수는", count, "개입니다.")