'''
문제 3 check3.py

    1kg -> 1000g
    무게 단위
    g       1000
    ton     0.001
    pound   2.204

    입력 : 100 (kg)
    출력 : 0.1 (ton)
'''

units = {'g' : 1000
       , 'ton' : 0.001
       , 'pound' : 2.204}
user = input("입력 : ")
value, unit = user.split()
result = 0
result = float(value) * units[unit]
print(result)